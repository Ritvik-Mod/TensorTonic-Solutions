import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    """
    # u = np.array(u,dtype=np.float64)[:,None]
    # v = np.array(v, dtype=np.float64)[None,:]
    # return u@v

    u = np.array(u,dtype=np.float64)
    u = u.reshape(u.shape[0],1)
    v = np.array(v, dtype=np.float64)
    v = v.reshape(v.shape[0],1)
    return u@(v.T)