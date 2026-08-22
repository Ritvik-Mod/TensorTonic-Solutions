import numpy as np

def gram_schmidt(vectors):
    """
    Returns: float64 array of shape (k, n), orthonormal basis spanning the input space.
    """
    # vectors --> (k,n) 1<=k<=n
    # all i/p vectors --> linearly independent
    # return (k,n) --> such that rows are mutually orthogonal vectors
    # |
    # |
    #  --> q1, q2, q3, .... , qk in the order they were produced
    # so each row is a vector thats given to us
    
    vectors = np.array(vectors,dtype=np.float64)
    orth = vectors.copy()
 
    for i in range(len(vectors)):
        v_k = vectors[i]
        orth[i] = vectors[i] - np.sum([( (np.dot(v_k,orth[j]))/(np.dot(orth[j],orth[j])))*(orth[j]) for j in range(i) ],axis=0)
        orth[i] = orth[i] / np.linalg.norm(orth[i])
    
    return orth