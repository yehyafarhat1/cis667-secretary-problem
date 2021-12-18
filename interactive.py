## This file is to run test interactively
import copy
import random

import histogram_representation
import number_helpers
from algorithms import domain_impl
from generator import DataGenerator
from recorder import Recorder
from memory_profiler import profile


class InteractiveTester:
    def __init__(self):
        start = random.randint(1, 10)
        end = random.randint(20, 99)
        self.generator = DataGenerator(start, end)
        self.round_number = random.randint(start, end)
        self.player_score = 0
        self.ai_score = 0
        pass

    # @profile
    def start_test(self, model):
        print("Now start playing with {exp_name} ...... \r\n".format(
            exp_name=model.name()))

        model_instance = copy.deepcopy(model)
        best_value = 0.0
        player_best_value = 0
        player_selected = False
        model_best_value = 0

        for round in range(0, self.round_number):
            val = self.generator.next_val()
            best_value = max(best_value, val)
            print("Current round: {round} \t Current candidate value: {val} \t best value={best}"
                  "\t Your score: {player_score} \t AI score: {ai_score} ".format(
                round=round + 1, val=val, player_score=self.player_score,
                best=best_value,
                ai_score=self.ai_score))

            hints = "Choose or not. Input 1 to choose the current candidate, otherwise continue," \
                    " 0 to end the game. "
            user_input = input(hints)
            is_num, num_val = number_helpers.to_int_tuple(user_input)

            if is_num and num_val == 0:
                break
            elif is_num and num_val == 1 and player_selected == False:
                # select
                player_selected = True
                player_best_value = val
                pass
            else:
                # don't select, next round
                pass

            model_selected, v_value = model_instance.decide(round, val)
            print('model_selected:{sel}   {val}'.format(sel=model_selected, val=v_value))
            if model_selected:
                model_best_value = val

            if player_selected or model_selected:
                if player_best_value == model_best_value:
                    print("Both sides have the same candidate best value; next\r\n")
                    # no points
                else:
                    if player_best_value > model_best_value:
                        if player_best_value >= best_value:
                            self.player_score += 3
                        else:  # player_best_value < best_value
                            self.player_score += 1
                    else:  # player_best_value < model_best_value
                        if model_best_value >= best_value:
                            self.ai_score += 3
                        else:  # model_best_value < best_value
                            self.ai_score += 1

                    print("Your best {player_best}; AI best {ai_best};\t"
                          " Your score: {player_score} \t AI score: {ai_score}  next\r\n"
                          .format(player_best=player_best_value,
                                  ai_best=model_best_value,
                                  player_score=self.player_score,
                                  ai_score=self.ai_score))
            else:
                print("no action; next\r\n")

        print("Final result: \r\n")
        print("Round: {round} \t; Best value={best}"
              "\t Your score: {player_score} \t AI score: {ai_score} "
              .format(round=self.round_number, best=best_value,
                      player_score=self.player_score,
                      ai_score=self.ai_score))
