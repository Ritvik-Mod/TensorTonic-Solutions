import numpy as np

def vector_projection(u, v):
    """
    Returns: float64 array, the projection of u onto v.
    """
    u, v = np.array(u,dtype=np.float64), np.array(v,dtype=np.float64)
    return (np.dot(u,v)/np.dot(v,v))*v