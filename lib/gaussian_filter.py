from __future__ import division

import numpy as np
from scipy.signal import convolve2d

def g(x, mu, sigma):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sigma, 2.)))

def gauss_kernel(**kwargs):
    s       = kwargs.get('size',    3)
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   2.0)

    x       = np.array(range(-s,s+1))
    xx      = np.array([x*x])
    m       = np.sqrt(xx + xx.T)
    m      /= np.sum(m)

    return g(m, mu, sigma)

def gaussian(img, **kwargs):
    s       = kwargs.get('size',    3)
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   2.0)

    return convolve2d(img, gauss_kernel(size=s, mu=mu, sigma=sigma), mode="same", boundary="symm")
