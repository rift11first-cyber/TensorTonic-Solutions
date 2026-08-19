import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X,dtype=float)
    mx = X.max(axis=axis,keepdims=True)
    mn = X.min(axis=axis,keepdims=True)
    return ((X-mn)/(mx-mn+eps)).tolist()