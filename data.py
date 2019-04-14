import torch
import pandas as pd
import numpy as np
import numpy.random as rand
from torch.utils.data import DataLoader, Dataset, TensorDataset
from sklearn.model_selection import train_test_split


class Generator:

    def __init_