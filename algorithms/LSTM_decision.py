import algorithms.LSTM
import random
import numpy as np
import torch as tr
import os
import pickle


class LstmDecisionAlgorithm1:
    def __init__(self):
        self.norm_hist_candidates = []
        self.list_historical_candidates = []
        self.net = tr.load('./algorithms/net20211217.torch')
        # with open('./algorithms/net20211217.pkl', 'rb') as infile:
        #     self.net = pickle.load(infile)
        pass

    def name(self):
        return "LSTM Decision Algorithm net20211217"

    def __str__(self, self_print=False, print_nodes=False):
        str_result = "Search nodes not applicable\r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):
        # if current_index <= 20:
        #     return False, current_value

        dt2 = round(self.norm(current_value, 0, 10))
        self.norm_hist_candidates.append(dt2)
        self.list_historical_candidates.append(current_value)
        (x, y) = self.net.make_decision(np.array([dt2]))

        if x is not None and y is not None and x < dt2:
            # x is the most likely value in the appeared candidates
            value = self.list_historical_candidates[x]
            if current_value >= value:
                return True, current_value

        # fake implementation to ensure LSTM algorithm integration
        return False, current_value

    def norm(self, dt, left, right):
        dt2 = dt / 100.0
        range = right - left
        return left + (range * dt2)
