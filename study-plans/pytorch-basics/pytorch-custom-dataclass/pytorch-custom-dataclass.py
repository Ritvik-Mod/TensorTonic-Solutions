import torch
from torch.utils.data import Dataset

class CSVDataset(Dataset):
    """
    Returns: (features, label) from __getitem__ where features is float32 (D,) and label is float32 (1,)
    """

    def __init__(self, data, label_col):
        self.data = torch.tensor(data,dtype=torch.float32)
        self.label_col = torch.tensor(label_col,dtype=torch.int32).item()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):

        op1 = torch.concat((self.data[idx,0:self.label_col],self.data[idx,self.label_col+1:]))

        op2 = self.data[idx,self.label_col].unsqueeze(0)

        return (op1,op2)
