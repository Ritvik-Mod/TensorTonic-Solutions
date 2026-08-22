import torch

def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Returns: tensor of shape (N, D), the batch-normalized output
    """
    X = torch.tensor(X) #(N,D)
    gamma = torch.tensor(gamma)
    beta = torch.tensor(beta)
    u_j = torch.sum(X,dim=0)/X.shape[0] #(D,)
    var = torch.sum((X - u_j)**2,dim=0)/X.shape[0] #(D,)
    X_cap = (X - u_j)/(torch.sqrt(var + eps))
    Y = gamma*X_cap + beta
    return Y