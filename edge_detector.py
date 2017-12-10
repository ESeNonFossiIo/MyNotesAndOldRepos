import sys
sys.path.append("./lib/")

from PIL import Image
import numpy as np
from matplotlib.pyplot import imshow, show, subplot, savefig, figure, gray, title, gray, axis

from lib.filters import gaussian_filter, gradient_filter, nonmax_suppression, thresholding

name="./img/Lena"
ext=".jpg"

img=name+ext
print " > Processing -> ", img


im = np.array(Image.open(img))
im = im[:, :, 0]

print "     > Gaussian filter "
g_filter               = gaussian_filter(im, s=2, sigma=2.0)
print "     > Gradient filter "
gradient_img, tan_img  = gradient_filter(g_filter)
print "     > Non Max Suppression filter "
loc_max                = nonmax_suppression(gradient_img, tan_img)
print "     > Double Thresholding filter "
thresholding           = thresholding(loc_max, lo_val = 0.1 , hi_val=0.3)

print "     > Edge Tracking "
edge    = np.zeros(thresholding.shape)
max_val = np.max(thresholding)

t_max = np.max(thresholding)
edge[thresholding==t_max]=1.0

def track_max(edge, thresh, x, depth, directions):
    if depth < 1:
        return
    for a in directions:
        d = np.rint([np.cos(a), np.sin(a)]).astype(int)
        i,j = x+d
        if 0 <= i < thresh.shape[0]  and 0 <= j < thresh.shape[0]:
            if  0.1 < thresh[i,j] < 1:
                edge[i,j] = 1.0
                track_max(edge, thresh, np.array([i,j]), depth - 1, [a, a + np.pi/4, a - np.pi/4])

old_ones_len = 0
directions   = np.array(range(4))*np.pi/2
while True:
    ones = [(i,j) for i,j in np.concatenate(np.where(edge == 1.0)).reshape(2,-1).T]
    for p in ones:
        i, j = p
        edge[i,j] += 1.0
    for p in ones:
        i, j = p
        track_max(edge, thresholding, np.array([i,j]), 10, directions)
    if old_ones_len == len(edge[edge>0]):
        break
    else:
        old_ones_len = len(edge[edge>0])

edge[edge>0] = 1.0

print "     > Done! "

################################################################################
#Image Output ##################################################################
################################################################################

gray()

axis('off')
imshow(im)
show()

axis('off')
imshow(g_filter)
savefig(name+"_blur"+ext)
show()

axis('off')
imshow(gradient_img)
savefig(name+"_grad_magnitude"+ext)
show()

axis('off')
imshow(tan_img)
savefig(name+"_grad_orientation"+ext)
show()

axis('off')
imshow(loc_max)
savefig(name+"_non_nam_suppression"+ext)
show()

axis('off')
imshow(thresholding)
savefig(name+"_thresholding"+ext)
show()

axis('off')
savefig(name+"_edge"+ext)
imshow(edge)
show()
