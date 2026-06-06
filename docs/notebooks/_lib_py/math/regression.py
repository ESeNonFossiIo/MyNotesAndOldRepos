from numpy import array, dot
from numpy.linalg import inv

def regression(x, y, order = 2):
    """ Compute the regression function of (x, y)
        using a polynomial of order degree

        Args:
            x(np.array): independent variable
            y(np.array): dependent variable
            order(int): order of the regression. default = 2

        Return:
            np.array: coefficients of the regression
    """
    # Vandermonde matrix:
    V = array([x] * (order + 1)).T**range(order + 1)
    Vt = V.transpose()

    # compute coeff
    return dot(dot(inv(dot(Vt, V)), Vt), y)
