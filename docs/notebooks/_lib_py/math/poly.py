from numpy import sum, array

def eval_poly(c, x):
    """ Evaluate the c-coefficients polynomial at x

        Args:
            c (np.array): coefficients
            x (np.array): where to evaluate the poly at

        Returns:
            (float): value of the evaluations
    """
    assert len(c) > 1, "c can be an empty array"
    order = len(c) - 1
    
    return sum(c * array([x] * (order + 1)).T**range(order + 1), axis=1)
