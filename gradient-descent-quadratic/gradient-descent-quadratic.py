def der(a,b,c,x0):
    return (2*a*x0)+(b)

def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    for i in range(steps):
        deri = der(a,b,c,x0)
        x0 = x0 - lr*deri
    return x0