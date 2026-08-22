import numpy as np

def matrix_transpose(A):
    """
    Returns: ndarray, the transpose of A.
    """
    A = np.array(A)
    B = np.empty((A.shape[1],A.shape[0]))
    for i in range(A.shape[1]):
        B[i] = A[:,i]
    return B