import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    return np.sqrt(np.sum((np.array(x)-np.array(y))**2,dtype=np.float64))