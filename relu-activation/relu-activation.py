import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.asarray(x,dtype=float)
    return np.where(x<=0,0,x)