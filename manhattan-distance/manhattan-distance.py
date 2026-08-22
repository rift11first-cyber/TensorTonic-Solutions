import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Return the Manhattan distance between x and y.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    y = np.asarray(y,dtype=float)
    return float(np.sum(np.abs(x-y)))