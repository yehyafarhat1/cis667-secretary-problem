import random


class DataGenerator:
    def __init__(self, data_min_inclusive, data_max_inclusive):
        self.data_min_inclusive = data_min_inclusive
        self.data_max_inclusive = data_max_inclusive
        self.rand_operator = random
        pass

    def next_val(self):
        val = self.rand_operator.random()
        val = val * (self.data_max_inclusive - self.data_min_inclusive) + self.data_min_inclusive
        return val
