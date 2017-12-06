import numpy as np
from scipy.signal import convolve2d

def sobel_operators():
    x = np.array([[1,2,1]])
    y = np.array([range(-1,2,1)])
    return x.T*y, (x.T*y).T

def gradient(img):
    sox, soy = sobel_operators()
    Dx      = convolve2d(img, sox, mode="same", boundary="symm")
    Dy      = convolve2d(img, soy, mode="same", boundary="symm")
    D       = np.sqrt(Dx*Dx + Dy*Dy)
    Theta   = np.arctan(Dy, Dx) * 180.0 / np.pi
    return D, Theta
