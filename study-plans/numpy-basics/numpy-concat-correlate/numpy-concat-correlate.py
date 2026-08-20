import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a = np.array(a,dtype=np.float64)
    b = np.array(b, dtype = np.float64)

    conc = np.concatenate([a,b],axis=0)

    a_corr = np.corrcoef(a,rowvar=False) #variables are columns so forms nxn o/p
    b_corr = np.corrcoef(b,rowvar=False)
    conc_corr = np.corrcoef(conc,rowvar=False)

    return np.stack([a_corr,b_corr,conc_corr])