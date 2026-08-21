import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.array(v,np.float64)
    euc_l2norm = np.linalg.norm(v)
    man_l1norm = np.sum(abs(v))
    l_inf_norm = np.max(abs(v))

    return np.array([man_l1norm,euc_l2norm,l_inf_norm])