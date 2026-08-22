import torch

def gradient_accumulation(w_init, micro_batches, lr, accum_steps):
    """
    Returns: tuple of (updated_weights_list, last_avg_gradient_list)
    """
    w = torch.tensor(w_init,dtype=torch.float32,requires_grad=True)
    grada = 0
    for i, (inputs,target) in enumerate(micro_batches):
        inputs = torch.tensor(inputs).to(torch.float32)
        target = torch.tensor(target).to(torch.float32)
        loss = torch.mean(((w@inputs.T)-target)**2,dim=-1)
        loss.backward()
        if((i+1)%accum_steps==0):
            w.grad = w.grad/accum_steps
            grada = w.grad.clone().detach()
            w = w - lr*w.grad
            w = torch.tensor(w,requires_grad=True)
    return (w.tolist(),grada.tolist())