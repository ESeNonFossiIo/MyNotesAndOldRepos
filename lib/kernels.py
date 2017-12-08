from functions import gaussian

from numpy import array, sqrt
from numpy import sum as npsum

def gaussian_kernel(**kwargs):
    s       = kwargs.get('size',    2)
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   1.0)
    integer = kwargs.get('integer', False)

    x       = array(range(-s,s+1))
    xx      = array([x*x])
    m       = sqrt(xx + xx.T)
    m      /= npsum(m)

    if integer:
        g   = gaussian(m, mu=mu, sigma=sigma)
        gi  = (g*(1/g[0,0])).astype(int)
        return gi, npsum(gi)
    else:
        return gaussian(m, mu=mu, sigma=sigma), 1.0

def sobel_kernel():
    x = array([[1,2,1]])
    y = array([range(-1,2,1)])
    return x.T*y, (x.T*y).T
