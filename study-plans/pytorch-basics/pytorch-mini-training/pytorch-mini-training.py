import torch
import torch.nn as nn

def train_epoch(model, dataloader, criterion, optimizer):
    """
    Returns: average loss over all batches (float)
    """
    loss_m = []
    for inputs, targets in dataloader:
        predictions = model(inputs)
        lb = criterion(predictions,targets)
        loss_m.append(lb)
        optimizer.zero_grad()
        lb.backward()
        optimizer.step()
    loss_m = torch.tensor(loss_m)
    return torch.mean(loss_m).item()