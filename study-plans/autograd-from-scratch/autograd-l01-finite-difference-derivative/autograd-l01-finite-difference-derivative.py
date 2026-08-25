import numpy as np

def f(c,x):
    # return np.dot(c,x**np.array([i for i in range(len(c))]))
    return np.sum(np.polyval(c[::-1],x))

def finite_difference_derivative(coefficients, x, h):
    """
    Returns: the polynomial value at x, the value at x plus h, and the forward-difference slope
    """
    
    at_x = f(coefficients,x)
    at_x_h = f(coefficients,x+h)
    forward_diff_slope = (at_x_h - at_x)/h
    return (at_x,at_x_h,forward_diff_slope)