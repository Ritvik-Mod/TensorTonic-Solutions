import torch
from torch.utils.data import DataLoader, TensorDataset, WeightedRandomSampler

def create_balanced_loader(features, labels, batch_size):
    """
    Returns: a DataLoader that oversamples underrepresented classes
    """
    dataset = TensorDataset(features,labels)
    freq = torch.bincount(labels)
    sample_weights = []
    for label in labels:
        sample_weights.append(1/freq[label])
    sampler = WeightedRandomSampler(weights = sample_weights, num_samples = len(dataset))
    data_loader = DataLoader(dataset,batch_size=batch_size,sampler = sampler)
    return data_loader