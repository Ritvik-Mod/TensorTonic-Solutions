import numpy as np

def matrix_trace(A):
    """
    Returns: float, the trace (sum of diagonal elements) of A.
    """
    A = np.array(A)
    trace = np.array([(A[i,i]) for i in range(A.shape[0])])
    return np.sum(trace)