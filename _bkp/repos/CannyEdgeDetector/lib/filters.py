from __future__ import division

from scipy.signal import convolve2d

from numpy import sqrt, arctan2, pi, power
from numpy import zeros, concatenate, where
import numpy as np

from kernels import gaussian_kernel, sobel_kernel

def gaussian_filter(img, **kwargs):
    s       = kwargs.get('size',    2)
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   1.4)
    gk, gks = gaussian_kernel(size=s, mu=mu, sigma=sigma)
    return convolve2d(img, gk/gks, boundary='symm', mode='same')

def gradient_filter(img):
    sox, soy = sobel_kernel()
    Dx       = convolve2d(img, sox, boundary='symm', mode='same')
    Dy       = convolve2d(img, soy, boundary='symm', mode='same')

    D        = sqrt(Dx*Dx + Dy*Dy)
    Theta    = arctan2(abs(Dy), abs(Dx))

    return D, Theta

def nonmax_suppression(magnitude, phase):
  p = phase.copy()
  p = ((p + 2 * pi + pi/8) % pi) // (pi/4)
  n = [np.rint([np.sin(a), -np.cos(a)]) for a in np.array(range(0,4))*np.pi/4]

  loc_max = zeros(magnitude.shape)
  for i in xrange(1, loc_max.shape[0] - 1):
    for j in xrange(1, loc_max.shape[1] - 1):
      ni, nj = np.rint(n[int(p[i][j])]).astype(int)
      if  magnitude[i][j] >= magnitude[i + ni][j + nj] \
          and magnitude[i][j] >= magnitude[i - ni][j - nj]:
        loc_max[i][j] = magnitude[i][j]
  return loc_max

def thresholding(im, **kwargs):
  thres  = im.copy()
  thres  /= np.max(im)

  lo = kwargs.get("lo_val",  .1)
  hi = kwargs.get("hi_val",  .7)

  thres[ thres <= lo ] = lo
  thres[ thres >= hi ] = hi

  return thres
