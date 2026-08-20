import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    data = np.array(data,dtype=np.float64)
    data_round = np.pad(np.round(data,decimals=decimals),pad_width=pad_width)
    data_floor = np.pad(np.floor(data),pad_width=pad_width)
    data_ceil = np.pad(np.ceil(data),pad_width=pad_width)

    return np.stack([data_round,data_floor,data_ceil])