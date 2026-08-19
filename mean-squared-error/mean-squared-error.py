import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    p = np.asarray(y_pred,dtype=float)
    t = np.asarray(y_true,dtype=float)
    return float(np.mean((p-t)**2))
