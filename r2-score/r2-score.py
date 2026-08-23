import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """Return the coefficient of determination."""
    # Write code here
    t = np.asarray(y_true,dtype=float)
    p = np.asarray(y_pred,dtype=float)
    a = np.sum((t-p)**2)
    n = np.sum((t-np.mean(t))**2)
    if n ==0 :
        return 1.0 if a == 0 else 0.0
    return float(1.0 - a/n)