import numpy as np

def thresholding(im, **kwargs):
    thres  = np.zeros(im.shape)
    strong = kwargs.get("strong", 1.0)
    weak   = kwargs.get("weak",    .5)
    lo_val = kwargs.get("lo_val",  .1)
    hi_val = kwargs.get("hi_val",  .8)

    mmax   = np.max(im)
    lo, hi = lo_val * mmax, hi_val * mmax

    # TODO: controllare questo passaggio
    thres[ im >= lo ] = weak
    thres[ im >= hi ] = strong

    strongs = [(i,j) for i,j in np.concatenate(np.where(im>=hi)).reshape(2,-1).T]
    return thres, strongs
