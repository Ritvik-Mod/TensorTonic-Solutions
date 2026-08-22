import numpy as np

def matrix_multiply(A, B):
    """
    Returns: 2-D float64 array, the matrix product A @ B.
    """
    A = np.array(A)
    B = np.array(B)
    C = np.empty((A.shape[0],B.shape[1]))

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            C[i,j] = np.sum(A[i]*B[:,j])
    return C