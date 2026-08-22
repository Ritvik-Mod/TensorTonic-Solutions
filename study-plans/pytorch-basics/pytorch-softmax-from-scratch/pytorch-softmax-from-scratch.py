import torch

def softmax(logits):
    """
    Returns: tensor of same shape with softmax probabilities (each row sums to 1)
    """
    #logits (N,C)
    logits = torch.tensor(logits)
    mi = torch.max(logits,dim=1).values #(N,)
    num = torch.exp(logits - mi[:,None]) #(N,C)

    den = torch.sum(torch.exp(logits-mi[:,None]),dim=1) #(N,)

    return num/den[:,None]