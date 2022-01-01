import torch.cuda

import algorithms.LSTM
import pickle
import os
import torch as tr
import numpy as np
from algorithms.LSTM1 import Net20211217
from torch import nn

if __name__ == "__main__":
    print("CUDA: "+str(torch.cuda.is_available()))
    print("GPUs: "+str(torch.cuda.device_count()))
    algorithms.LSTM1.self_train()
    pass