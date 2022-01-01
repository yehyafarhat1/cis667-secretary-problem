## This file is to run test automatically
import copy
import random

import histogram_representation
from algorithms import domain_impl
from generator import DataGenerator
from recorder import Recorder
from memory_profiler import profile


class AutomaticTester:
    def __init__(self, size=4):
        self.total_test_sizes = size + 1
        start = random.randint(1, 10)
        end = random.randint(20, 99)
        self.generator = DataGenerator(start, end)
        pass

    # @profile
    def start_test(self, model):
        print("Now start experiment with {exp_name} ...... \r\n".format(
            exp_name=model.name()))

        recorder_list = []

        # to make experiments faster,
        # temporary disable size 5 which causes more than 100000 steps per game
        for size in range(1, self.total_test_sizes):
            print("Test with size {size_str}\r\n"
                  .format(size_str=domain_impl.get_size_str(size)))

            # one game, one recorder
            for game in range(1, 101):
                if game % 10 == 0 or size > 4:  # when size > 4, print every time
                    print("Game {game} with size {size_str}".format(
                        game=game.__str__(), size_str=domain_impl.get_size_str(size)))
                recorder = Recorder()

                stop_point = domain_impl.calculate_random_stop_point(size)
                domain_algo = copy.deepcopy(domain_impl.Prime_37percent())
                model_instance = copy.deepcopy(model)

                best_val = -9999999.99

                for round in range(0, stop_point):
                    val = self.generator.next_val()

                    best_val = max(best_val, val)

                    domain_selected, domain_best_value = domain_algo.decide(round, val)
                    model_selected, model_best_value = model_instance.decide(round, val)

                    recorder.append({"size": size, "game": game, "index": round,
                                     "value": val, "best_value": best_val,
                                     "domain_selected": domain_selected,
                                     "domain_best_value": domain_best_value,
                                     "model_selected": model_selected,
                                     "model_best_value": model_best_value})
                    pass

                recorder_list.append(recorder)
            pass

            # one size, one comparison
            self.compare_and_create_diagrams(recorder_list)

    def compare_and_create_diagrams(self, recorder_list):
        represent = histogram_representation.HistogramRepresentation()
        represent.histogram(recorder_list)
        pass
