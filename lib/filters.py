from __future__ import division

from scipy.signal import convolve2d

from numpy import sqrt, arctan2, pi
from numpy import zeros, concatenate, where
import numpy as np

from kernels import gaussian_kernel, sobel_kernel

def gaussian_filter(img, **kwargs):
    s       = kwargs.get('size',    3)
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   2.0)
    gk, gks = gaussian_kernel(size=s, mu=mu, sigma=sigma)
    return convolve2d(img, gk/gks, mode="same", boundary="symm")

def gradient_filter(img):
    sox, soy = sobel_kernel()
    Dx       = convolve2d(img, sox, mode="same", boundary="symm")
    Dy       = convolve2d(img, soy, mode="same", boundary="symm")

    D        = sqrt(Dx*Dx + Dy*Dy)
    Theta    = arctan2(Dy, Dx)

    return D, Theta

def nonmax_suppression(val, phase):
  loc_max = zeros(val.shape)
  for i in xrange(1, loc_max.shape[0] - 1):
    for j in xrange(1, loc_max.shape[1] - 1):
      for a in np.array(range(4))*np.pi/4:
        if (phase[i][j] <= a + np.pi/4 and phase[i][j] > a - np.pi/4) or (phase[i][j] <= a + np.pi + np.pi/4 and phase[i][j] > a + np.pi - np.pi/4) :
          d = np.rint([np.cos(a), np.sin(a)])
          n = np.array([d[1], -d[0]]).astype(int)
          if val[i][j] >= val[i + n[0]][j + n[1]] or val[i][j] >= val[i - n[0]][j - n[1]]:
            loc_max[i][j] = val[i][j]
          break
  return loc_max

def thresholding(im, **kwargs):
  thres  = im.copy()
  thres  /= np.max(im)

  lo = kwargs.get("lo_val",  .1)
  hi = kwargs.get("hi_val",  .7)

  thres[ im <= lo ] = 0.0
  thres[ im >= hi ] = 1.0

  return thres
