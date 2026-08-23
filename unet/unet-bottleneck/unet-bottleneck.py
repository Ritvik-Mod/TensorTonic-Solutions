import numpy as np

def unet_bottleneck(x: np.ndarray, out_channels: int) -> np.ndarray:
    """
    U-Net bottleneck: double convolution at lowest resolution.
    Two 3x3 unpadded convolutions, no pooling.
    Returns zero array with correct shape.
    """
    # Your implementation here
    return np.zeros((x.shape[0], x.shape[1]-4, x.shape[2]-4, out_channels))