import numpy as np

def encoder(x):
    n,h,w,c = x.shape
    h = (h-4)//2
    w = (w-4)//2
    c = c*2
    return (n,h,w,c)

def decoder(x):
    n,h,w,c = x.shape
    h = 2*h - 4
    w = 2*w - 4
    c = c//2
    return (n,h,w,c)

def bottleneck(x):
    n,h,w,c = x.shape
    h = h-4
    w = w-4
    c = c*2
    return (n,h,w,c)

def output(x,num_classes):
    n,h,w,_ = x.shape
    return (n,h,w,num_classes)

def unet(x: np.ndarray, num_classes: int = 2) -> np.ndarray:
    """
    Complete U-Net: trace shape through 4 encoder blocks, bottleneck, 4 decoder blocks, output.
    Each block: two 3x3 unpadded convs (reduce by 4), encoder pools (halve), decoder upsamples (double).
    Returns zero array with correct output shape.
    """
    # Your implementation here
    # 4 encoder blocks --> each h-4 then h//2 after max pool --> c*2
    # 1 bottleneck block
    # 4 decoder blocks - with skip connections --> each 2*h-4 --> c//2
    # 1 output layer --> same b,h,w | c = num_classes

    #pass to encoder block 1:
    x = np.zeros(encoder(x))
    #pass to encoder block 2:
    x = np.zeros(encoder(x))
    #pass to encoder block 3:
    x = np.zeros(encoder(x))
    #pass to encoder block 4:
    x = np.zeros(encoder(x))

    #pass to bottleneck block:
    x = np.zeros(bottleneck(x))

    #pass to decoder block 1:
    x = np.zeros(decoder(x))
    #pass to decoder block 2:
    x = np.zeros(decoder(x))
    #pass to decoder block 3:
    x = np.zeros(decoder(x))
    #pass to decoder block 4:
    x = np.zeros(decoder(x))

    #pass to output block:
    x = np.zeros(output(x,num_classes))

    return x