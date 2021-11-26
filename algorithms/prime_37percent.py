import math
import sys


class Prime_37percent:
    def __init__(self):
        self.current_best_val = sys.float_info.min
        self.current_best_index = -1
        self.current_iteration_count = 0
        self.list_historical_candidates = []
        pass


    def name(self):
        return "Prime 37 percent algorithm"

    def __str__(self, self_print = False):
        str_result = "Override of str function\r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):
        self.list_historical_candidates.append(current_value)

        list_prev_37per = self.list_historical_candidates[:
            math.ceil(self.list_historical_candidates.__len__() * 0.37)]

        if list_prev_37per.__len__() > 0:
            whether_select = max(list_prev_37per) < current_value #and self.current_best_val < current_value
            if whether_select:
                self.current_best_val = current_value
                self.current_best_index = current_index
                return True, current_index

        return False, self.current_best_index