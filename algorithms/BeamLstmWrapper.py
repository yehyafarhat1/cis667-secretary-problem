import random
import numpy as np
import torch as tr
import math
import pickle


# Define a small LSTM recurrent neural network with linear hidden-to-output layer
class BeamLstmWrapper():
    def __init__(self, modelname='', word_path='', dictionary_path = '', net_path= ''):
        self._name = modelname
        self._words = []
        self.dictionary = {}
        with open(word_path, 'rb') as handle1:
            self._words = pickle.load(handle1)  # like_people is a list with data
        with open(dictionary_path, 'rb') as handle2:
            self.dictionary = pickle.load(handle2)  # like_people is a list with data

        self.net = None

        self.net = tr.load(net_path)

        self.norm_hist_candidates = []
        self.list_historical_candidates = []
        pass

    def name(self):
        return self._name

    def __str__(self, self_print=False, print_nodes=False):
        str_result = "Search nodes not applicable\r\n"
        if self_print is not None and True == self_print:
            print(str_result)
        return str_result

    ## return true or false , selected index
    def decide(self, current_index, current_value):
        dt2 = round(self.norm(current_value, 0, 10))
        self.norm_hist_candidates.append(dt2)
        self.list_historical_candidates.append(current_value)

        # real prediction
        current_sentence = self.norm_hist_candidates # ['3', '5', '7', '4', '3', '2']
        v = None
        # print(current_sentence)
        # keep the final(last word) prediction
        final_word = None
        final_y = None
        final_y_args = None
        final_val = 0
        final_prob = 0

        for c in current_sentence:
            x = self.dictionary[c]

            print('x={x}'.format(x=x))
            print('----------------------------------------')
            y, v = self.net(self.dictionary[c], v)

            y = y.squeeze()  # ignore singleton dimensions for time-step/example

            y.argmax()
            w = y.argmax()

            print('y={y}, v={v}, w={w}'.format(y=y, v=v, w=w))
            print('----------------------------------------')

            word = self._words[w]
            print('word={word} + w={w} ++ {words}'.format(word=word, w=w, words=self._words))
            print('----------------------------------------')
            prob = y[w]
            print(word, prob.item())
            print('----------------------------------------')

            final_word = word
            final_y = y
            final_y_args = np.argpartition(y, -5)

        prob_sum = np.sum(final_y_args)
        #in this line, the y has different probabilities,
        #but get 5 largest and calculate the expected value as the prediction
        for arg in final_y_args:
            word2 = self._words[arg] #word is string, we need integer
            word_f = float(word2)
            word_exp = word_f * final_y[arg]
            final_val += word_exp


        # all the probabilities need to be normalized to be the summation of 1
        final_prob = prob.item()


        if x is not None and y is not None and x > 0 and x < len(self.list_historical_candidates):
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

