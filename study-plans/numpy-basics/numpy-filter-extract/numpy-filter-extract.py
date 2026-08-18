import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    a = np.array(data,dtype = np.float64)
    a = a[row_start:row_stop]

    a = a[a>threshold]
    return a