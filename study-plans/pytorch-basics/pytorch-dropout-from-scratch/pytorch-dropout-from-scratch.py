import torch
import torch.nn as nn

class Dropout(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p

    def forward(self, x):
        """
        Returns: tensor with dropout applied
        """
        # m = torch.bernoulli(torch.full_like(x,1-self.p))
        if not self.training:
            return x
        if self.p==1:
            return torch.zeros_like(x)
        
        u = torch.rand(size=x.shape)
        m = torch.where(u>=self.p,1,0)
        
        return (m*x)/(1-self.p)