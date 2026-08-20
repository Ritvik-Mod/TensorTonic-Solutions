import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""
    data = np.array(data,dtype=np.float64)
    
    data_tiled = np.tile(data,(reps,1))
    
    data_tiled_diff = np.diff(data_tiled,axis=0)
    
    data_tiled_diff_pad = np.pad(data_tiled_diff,((0,1),(0,0)))

    return np.stack([data_tiled, data_tiled_diff_pad])