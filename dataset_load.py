from typing import Literal
import torch
from torch import nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, Subset
from sklearn.model_selection import KFold
import pandas as pd
import matplotlib.pyplot as plt

def load_from_images(device: Literal['cuda'] | Literal['mps'] | Literal['cpu']):
    from torchvision import datasets, transforms

    transform = transforms.Compose([
        # transforms.Resize((256, 192)),
        # transforms.Resize((32, 32)),
        transforms.Resize((224, 224)),
        # transforms.Resize(224),
        transforms.ToTensor(),
        # transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    dataset = datasets.ImageFolder('datasets/3d-printer-defected-dataset', transform=transform)

    dataloader = torch.utils.data.DataLoader(
        dataset, 
        batch_size=32,
        pin_memory=True, # This is important for faster data transfer
        )
    
    return dataloader.dataset

def load_from_csv(device: Literal['cuda'] | Literal['mps'] | Literal['cpu']):
    # First we will load the csv, and separate the label
    defected = pd.read_csv("./defected.csv")
    not_defected = pd.read_csv("./not_defected.csv")

    data = pd.concat([defected, not_defected])

    print("Data shape: ", data.shape)

    metadata_columns = ('label', 'class', 'filename')

    train_x = data[3:].values
    labels = data['label'].values

    # Scale/normalize the data
    train_x_normalized = train_x / 255.0

    # Set up the model size params
    input_size = train_x_normalized.shape[1]
    output_size = 10
    print(f"{input_size=}, {output_size=}")

    # Convert the data into PyTorch dataset
    tensor_x = torch.tensor(train_x_normalized, dtype=torch.float32, device=device)
    tensor_y = torch.tensor(labels, dtype=torch.long, device=device) 

    dataset = TensorDataset(tensor_x, tensor_y)

    return dataset