import torch
import torch.nn as nn

def train_with_scheduler(model, dataloader, criterion, optimizer, scheduler, num_epochs):
    """
    Returns: dict with 'losses' (list of per-epoch avg loss) and 'lrs' (list of learning rate per epoch)
    """
    losses = []
    lrs = []
    for i in range(num_epochs):
        epoch_l = []
        for inputs,target in dataloader:
            pred = model(inputs)
            l = criterion(pred,target)
            epoch_l.append(l.item())
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        lrs.append(scheduler.get_last_lr()[0])
        scheduler.step()
        losses.append(sum(epoch_l)/len(epoch_l))
    return {'losses':losses, 'lrs':lrs}