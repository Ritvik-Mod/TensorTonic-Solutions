import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    data = np.array(data,dtype=np.float64)
    argmax = np.argmax(data,axis=1)
    argmin = np.argmin(data,axis=1)
    min = data.min(axis=1)
    max = data.max(axis=1)
    return np.stack([max,argmax,min,argmin])