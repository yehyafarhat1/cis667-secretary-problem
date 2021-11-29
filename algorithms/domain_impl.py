import math
import sys

from generator import DataGenerator

COL_Candidate_Index = "Candidate Index"
COL_Candidate_Value = "Candidate Value"
COL_Current_Best_Candidate_Value = "Current Best Candidate Value"
COL_Current_Best_Candidate_Index = "Current Best Candidate Index"



def get_size_str(size):
    if 1 < size <= 2:
        return "100~1000"

    if 2 < size <= 3:
        return "1000~5000"

    if 3 < size <= 4:
        return "5000~10000"

    if 4 < size <= 5:
        return "100000~1000000"

    return "10~100"


def calculate_random_stop_point(size):
    if 1 < size <= 2:
        gn = DataGenerator(100, 1000)
        return int(round(gn.next_val()))
        # return "100~1000"

    if 2 < size <= 3:
        gn = DataGenerator(1000, 5000)
        return int(round(gn.next_val()))
        # return "1000~5000"

    if 3 < size <= 4:
        gn = DataGenerator(5000, 10000)
        return int(round(gn.next_val()))
        # return "5000~10000"

    if 4 < size <= 5:
        gn = DataGenerator(100000, 1000000)
        return int(round(gn.next_val()))
        # return "100000~1000000"

    return int(round((DataGenerator(10, 100)).next_val()))
    # "10~100"

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