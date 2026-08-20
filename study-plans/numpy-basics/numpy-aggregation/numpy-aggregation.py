import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    data = np.array(data,dtype=np.float64)
    mean = np.mean(data,axis=axis)
    std = np.std(data,axis=axis)
    min = np.min(data,axis = axis)
    max = np.max(data,axis=axis)
    return np.stack([mean,std,min,max])