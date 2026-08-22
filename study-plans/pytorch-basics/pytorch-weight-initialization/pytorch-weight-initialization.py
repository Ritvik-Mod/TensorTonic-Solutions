import torch
from math import sqrt

def initialize_weights(fan_in, fan_out, method):
    """
    Returns: tensor of shape (fan_out, fan_in) with initialized weights
    """
    w = torch.empty(fan_out,fan_in)

    if method == 'xavier_uniform':
        w.uniform_(-sqrt(6/(fan_in+fan_out)),sqrt(6/(fan_in+fan_out)))

    if method == 'xavier_normal':
        w.normal_(0,sqrt(2/(fan_in+fan_out)))

    if method == 'he_uniform':
        w.uniform_(-sqrt(6/fan_in),sqrt(6/(fan_in)))

    if method == 'he_normal':
        w.normal_(0,sqrt(2/fan_in))

    return w