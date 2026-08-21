import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    x = np.array(x,dtype=np.float64)
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    max_freq = max(counts.values())
    res = [item for item,freq in counts.items() if freq==max_freq]
    res.sort()
    return {'mean':mean, 'median':median,'mode':res[0]}