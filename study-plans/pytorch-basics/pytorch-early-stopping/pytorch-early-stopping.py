import torch
import torch.nn as nn

def loss_compute(model,loader,criterion):
    loss = []
    with torch.no_grad():
        for inputs,target in loader:
            pred = model(inputs)
            l = criterion(pred,target)
            loss.append(l)
    loss = torch.tensor(loss,dtype=torch.float32)
    return torch.mean(loss).item()

def train_with_early_stopping(model, train_loader, val_loader, criterion, optimizer, max_epochs, patience):
    """
    Returns: dict with 'train_losses' (list), 'val_losses' (list), 'stopped_epoch' (int, 1-indexed)
    """
    # model --> instance of nn.Module
    # train_loader --> loads batches tuples of (inputs,targets) for train set
    # val_loader --> loads batches tuples of (inputs,targets) for val set
    # criterion --> loss function
    # optimizer --> torch.optim instance
    # max_epochs --> max no. of times to run training over all the batches in train_loader
    # patience --> limit before stopping training due to no improvement of loss
    train_l = []
    val_l = []
    counter = 0
    epoch = 0
    for i in range(max_epochs):
        epoch = i
        model.train()
        train_avg = []
        for inputs,target in train_loader:
            predictions = model(inputs)
            lb = criterion(predictions,target)
            train_avg.append(lb.item())
            lb.backward()
            optimizer.step()
            optimizer.zero_grad()

        model.eval()
        epoch_avg_train_loss = sum(train_avg)/len(train_avg)
        val_loss = loss_compute(model,val_loader,criterion)

        train_l.append(epoch_avg_train_loss)
        if(len(val_l)>=1):
            best_val = min(val_l)
            if(val_loss<best_val):
                counter=0
            else:
                counter+=1
                
        val_l.append(val_loss)
        
        if(counter>=patience):
            break
        
    return {'train_losses':train_l, 'val_losses':val_l,'stopped_epoch':epoch+1}