import numpy as np

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    p = np.polynomial.Polynomial([c,b,a])
    deriv = p.deriv()
    x = x0

    for _ in range(steps):
        x = x-lr*deriv(x)
    return x