import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    data = np.array(data,dtype=np.float64)
    lo_q = np.percentile(data,lo_q,axis=0)
    hi_q = np.percentile(data,hi_q,axis=0)

    #data --> (m,n)
    #lo_q --> (n,)
    #hi_q --> (n,)

    #need to convert lo_q and hi_q to (1,n) then clip so broadcasting does it for columns

    clipped = np.clip(data,lo_q[None,:],hi_q[None,:])

    lo_clip_mask = data<lo_q
    hi_clip_mask = data>hi_q

    return np.stack([clipped,lo_clip_mask,hi_clip_mask])