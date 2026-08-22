import numpy as np
def det(A):
    sum = 0
    if(A.shape[0]==1):
        return A[0,0]
    if(A.shape[0]==2):
        return (A[0,0]*A[1,1] - A[0,1]*A[1,0])
    
    for j in range(0,A.shape[0]):
        B = np.delete(A,0,axis=0)
        B = np.delete(B,j,axis=1)
        sum += ((-1)**(j))*det(B)*A[0,j]
    return sum
def matrix_determinant(A):
    """
    Returns: float, the determinant of square matrix A.
    """
    A = np.array(A)
    # return np.linalg.det(A)

    return det(A)