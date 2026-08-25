import numpy as np

def f(c,x):
    sum = 0.0
    for k,ck in enumerate(c):
        sum += ck*(x**k)
    return sum

def finite_difference_derivative(coefficients, x, h):
    """
    Returns: the polynomial value at x, the value at x plus h, and the forward-difference slope
    """
    
    at_x = f(coefficients,x)
    at_x_h = f(coefficients,x+h)
    forward_diff_slope = (at_x_h - at_x)/h
    return (at_x,at_x_h,forward_diff_slope)