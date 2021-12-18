import LSTM
import random
import numpy as np
import torch as tr


class LstmDecisionAlgorithm:
    def __init__(self):
        self.net = LSTM.Net(3)
        self.dictionary = { } # TODO: deserialize the dictionary from the model

        # TODO: complete algorithm integration
        population = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        weights = [0.05, 0.1, 0.05, 0.1, 0.3, 0.0, 0.1, 0.1, 0.1, 0.1]

        candidates = []

        for i in range(10):
            size = random.randint(2, 10)
            n = np.random.choice(11, 20, p=[0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.1])
            candidates.append(n)

        self.candidate_score = set()
        for z in candidates:
            for j in z:
                self.candidate_score.add(j)
        self.candidate_score = tuple(self.candidate_score)  # deterministic order

        self.tokens = {}

        I = tr.eye(len(self.candidate_score))
        dictionary = {
            word: I[w].reshape(1, 1, len(self.candidate_score))
            for w, word in enumerate(self.candidate_score)}
        pass

    def name(self):
        return "LSTM Decision Algorithm"

    def __str__(self, self_print=False, print_nodes=False):
        str_result = "Search nodes not applicable\r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):

        size = random.randint(2, 10)
        new_candidates = np.random.choice(11, size, p=[0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.1])

        print(new_candidates)

        score = new_candidates[0]
        v = None
        print(score)

        for t in range(len(new_candidates) - 1):
            x = self.dictionary[score]
            y, v = self.net(self.dictionary[self.tokens[t]], v)
            y = y.squeeze()  # ignore singleton dimensions for time-step/example
            w = y.argmax()
            single_candidate = self.candidate_score[w]
            prob = y[w]
            print(single_candidate, prob.item())

        #fake implementation to ensure LSTM algorithm integration
        return False, 0



