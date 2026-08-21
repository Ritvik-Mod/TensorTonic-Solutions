import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if(method=='zeros'):
        return torch.zeros(size=shape).tolist()
    if(method=='ones'):
        return torch.ones(size=shape).tolist()

    return torch.full(size=shape,fill_value=value).tolist()