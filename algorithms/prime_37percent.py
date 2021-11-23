import sys


class prime_37percent:
    def __init__(self):
        pass

    current_best_val = sys.float_info.min
    current_best_index = -1
    current_iteration_count = 0

    list_historical_candidates = []

    def name(self):
        return "Prime 37 percent algorithm"

    def print_self(self):
        print()
        pass

    ## return true or false , selected index
    def decide(self, current_index, current_value):
        self.current_best_val = max(
            self.list_historical_candidates[:int(self.list_historical_candidates.__len__() * 0.37)])
        self.current_best_index = self.list_historical_candidates.index(self.current_best_val)

        if self.current_best_val <= current_value:
            return True, current_index

        self.list_historical_candidates.append(current_value)

        return False, self.current_best_index