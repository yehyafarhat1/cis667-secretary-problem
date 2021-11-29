import math
import random
import sys

## This is an algorithm for test only
class FakeTreeSearch:
    def __init__(self):
        self.current_best_val = sys.float_info.min
        self.current_best_index = -1
        pass


    def name(self):
        return "Fake tree search algorithm"

    def __str__(self, self_print = False, print_nodes = False):
        str_result = "This is used to print search nodes\r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):

        number = random.random()
        if number < 0.37:
                self.current_best_val = current_value
                self.current_best_index = current_index
                return True, current_index

        return False, self.current_best_index