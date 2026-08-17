import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y = np.asarray(y_true,dtype=float)
    p = np.asarray(y_pred,dtype=float)
    e = y-p
    a = np.abs(e)
    l = np.where(a<=delta, 0.5*e**2 , delta*(a-0.5*delta))
    return float(np.mean(l))