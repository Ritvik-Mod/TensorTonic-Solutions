import torch
import torch.nn as nn

def manual_train_step(model, X, y, criterion, lr):
    """
    Returns: loss value as a Python float
    """
    # X --> input tensor --> float32
    # y --> target tensor --> float32
    # model --> model of instance nn.Module
    # criterion --> loss function
    # lr --> learning rate --> positive float

    y_cap = model(X)
    loss = criterion(y_cap,y)
    loss.backward()
    with torch.no_grad():
        for param in model.parameters():
            param.sub_(lr*param.grad)
            param.grad = None

    return loss.item()