import torch.cuda

import algorithms.LSTM
import pickle
import os
import torch as tr
import numpy as np
from algorithms.LSTM import Net20211217
from torch import nn

if __name__ == "__main__":
    print(torch.cuda.is_available())
    print(torch.cuda.device_count())
    algorithms.LSTM.self_train()
    pass