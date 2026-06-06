from __future__ import division

from functions import gaussian

from numpy import array, sqrt, outer
from numpy import sum as npsum

def gaussian_kernel(**kwargs):
    s       = kwargs.get('size',    2)
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   1.0)
    integer = kwargs.get('integer', False)

    x       = array(range(-s,s+1))
    g       = gaussian(x, mu=mu, sigma=sigma)
    m       = outer(g,g)

    if integer:
        gi  = (m/m[0,0]).astype(int)
        return gi, npsum(gi)
    else:
        return m, npsum(m)

def sobel_kernel():
    x = array([[1,2,1]])
    y = array([range(1,-2,-1)])
    return x.T*y, (x.T*y).T
