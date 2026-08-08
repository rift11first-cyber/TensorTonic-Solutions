import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x,dtype=float)
    s = 1.0 / (1.0 + np.exp(-x))
    r = x*s
    return np.round(r,4).tolist()