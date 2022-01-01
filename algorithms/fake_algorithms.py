import math
import random
import sys


## This is an algorithm for test only
class RandomAlgorithm:
    def __init__(self):
        self.current_best_val = sys.float_info.min
        self.current_best_index = -1
        pass

    def name(self):
        return "Random algorithm"

    def __str__(self, self_print=False, print_nodes=False):
        str_result = "Search nodes not applicable\r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):

        number = random.random()
        if number < 0.37:
            self.current_best_val = current_value
            self.current_best_index = current_index
            return True, self.current_best_val

        return False, self.current_best_val


class BeamSearchWithLSTM:
    def __init__(self):
        self.current_best_val = sys.float_info.min
        self.current_best_index = -1
        pass

    def name(self):
        return "Beam Search with LSTM"

    def __str__(self, self_print=False, print_nodes=False):
        str_result = "This is to show search nodes \r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):

        number = random.random()
        if number < 0.37:
            self.current_best_val = current_value
            self.current_best_index = current_index
            return True, self.current_best_val

        return False, self.current_best_val
