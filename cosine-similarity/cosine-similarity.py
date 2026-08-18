import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    if(np.sum(a)==0 or np.sum(b)==0):
        return 0
    return ( np.dot(a,b) / ( np.sqrt( np.sum(a**2) ) * np.sqrt( ( np.sum(b**2) ) ) ) )