import torch

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """
    pred = torch.tensor(pred)
    target = torch.tensor(target)
    if method=='mse':
        return ((target-pred)**2).to(torch.float32).mean().item()

    if method=='cross_entropy':
        maxi,_ = torch.max(pred,dim=1)
        rows = torch.arange(len(target))
        targ = pred[rows,target]
        li = maxi + torch.log(torch.sum(torch.exp(pred-maxi[:,None]),dim=1)) - targ
        return li.to(torch.float32).mean().item()

    if method=='huber':
        a = torch.abs(pred-target)
        l = torch.where(a<=delta, (a**2)/2, delta*(a-(delta/2)))
        return l.to(torch.float32).mean().item()