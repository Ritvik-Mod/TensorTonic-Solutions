import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x)
    if method=='relu':
        # return torch.max(torch.zeros_like(x),x).tolist()
        return torch.where(x>0, x, 0).tolist()
        
    if method=='sigmoid':
        return (torch.exp(x)/(1+torch.exp(x))).tolist()

    if method=='tanh':
        return (((torch.exp(x) - torch.exp(-x))/(torch.exp(x) + torch.exp(-x))) ).tolist()

    if method=='leaky_relu':
        # return torch.max(x,0.01*x).tolist()
        return torch.where(x>0, x, 0.01*x).tolist()