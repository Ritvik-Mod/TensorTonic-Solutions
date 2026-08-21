import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    x = np.array(x,dtype=np.float64)
    v = np.sum((x-np.mean(x))**2)/(len(x)-1)

    std = np.sqrt(v)

    return {'variance':v, 'std_dev':std}