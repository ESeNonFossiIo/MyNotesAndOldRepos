from __future__ import division

from numpy import exp, power, pi, sqrt

def gaussian(x, **kwargs):
    mu      = kwargs.get('mu',      0.0)
    sigma   = kwargs.get('sigma',   1.0)

    return 1/(sigma * sqrt(2*pi)) * exp(-power(x - mu, 2.) / (2 * power(sigma, 2.)))
