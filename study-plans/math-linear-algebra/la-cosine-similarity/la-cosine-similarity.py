import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    a = np.array(a,dtype=np.float64)
    b = np.array(b,dtype=np.float64)

    num = np.dot(a,b)
    den = (np.linalg.norm(a))*(np.linalg.norm(b))
    return num/den if den!=0 else 0