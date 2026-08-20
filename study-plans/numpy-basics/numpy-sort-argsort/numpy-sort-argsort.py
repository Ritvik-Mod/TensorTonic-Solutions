import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    data = np.array(data,dtype=np.float64)
    sort = np.sort(data,axis=axis)
    argsort = np.argsort(data,axis)
    return np.stack([sort,argsort])