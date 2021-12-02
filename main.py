import csv
import copy
import os
import io

import number_helpers
from algorithms.domain_impl import Prime_37percent
from algorithms.fake_algorithms import *
from generator import DataGenerator
from interactive import InteractiveTester
from test import AutomaticTester

domain_algorithm = Prime_37percent()

instance_a = RandomAlgorithm()
instance_b = BeamSearchWithLSTM()

supported_experiments_list = []
supported_experiments_map = {}
# TODO: Add all the experiment models here
supported_experiments_list.append(instance_a.name())
supported_experiments_map[instance_a.name()] = instance_a
supported_experiments_list.append(instance_b.name())
supported_experiments_map[instance_b.name()] = instance_b
# supported_experiments_list.append("Experiment B")
# supported_experiments_map["Experiment B"] = "This is B"
# supported_experiments_list.append("Experiment C")
# supported_experiments_map["Experiment C"] = "This is C"


#
# def read_preset_data(filename):
#     data_list = []
#     path_str = os.path.join("data", filename)
#     if os.path.exists(path_str):
#         with open(path_str, encoding="utf-8", mode='r') as csvFile:
#             readCSV = csv.reader(csvFile)
#             # skip header
#             next(readCSV)
#             # Candidate Index, Candidate Value, Current Best Candidate Value, Current Best Candidate Index
#             for row in readCSV:
#                 col1 = int(row[0])
#                 col2 = float(row[1])
#                 col3 = float(row[2])
#                 col4 = int(row[3])
#                 data_list.append({COL_Candidate_Index: col1,
#                                   COL_Candidate_Value: col2,
#                                   COL_Current_Best_Candidate_Value: col3,
#                                   COL_Current_Best_Candidate_Index: col4})
#
#     return data_list
#
#
# def write_one_row_format(is_selected, best_at_present, best_value_at_present, csv_row_dict):
#     print("Current:{index}; \t\t Value:{value}; \t Selected: {is_selected};"
#           " \t Best index now {best_at_present}; \t\t Best value now {best_value_at_present};"
#           " \t Optimal Value {optimal} \r\n".format(
#         index=csv_row_dict[COL_Candidate_Index].__str__().rjust(5, ' '),
#         value=csv_row_dict[COL_Candidate_Value].__str__().rjust(5, ' '),
#         is_selected=is_selected,
#         best_at_present=best_at_present, best_value_at_present=best_value_at_present.__str__().rjust(5, ' '),
#         optimal=csv_row_dict[COL_Current_Best_Candidate_Value].__str__().rjust(5, ' ')
#     ))
#
#
# def compare_and_result(csv_data):
#     print('--------------------------------------------------------------------------------------------------------')
#     print('========================================================================================================')
#     pass
#
#
# def run_one_dataset(model, csv_data):
#     model_instance = copy.deepcopy(model)
#     for i in range(0, len(csv_data)):
#         is_selected, best_at_present = model_instance.decide(i, csv_data[i][COL_Candidate_Value])
#         csv_data[i]["Is Selected"] = is_selected
#         csv_data[i]["Model Best at present"] = best_at_present
#         csv_data[i]["Model Best Value at present"] = \
#             csv_data[best_at_present][COL_Candidate_Value] if best_at_present >= 0 else 0
#         write_one_row_format(is_selected, best_at_present,
#                              csv_data[i]["Model Best Value at present"], csv_data[i])
#     compare_and_result(csv_data)


if __name__ == "__main__":
    strategy = input("To start the test case, input a number to determine which strategy to use.\r\n"
                     "Input non-number other numbers which are not included into this hints "
                     "to exit without running any experiments;\r\n"
                     "input 0 to start all the pre-set experiments automatically;\r\n"
                     "input 1 to start interactive experiments.;\r\n"
                     "")  # Python 3
    # raw_input("......")  # Python 2

    is_num, num = number_helpers.to_int_tuple(strategy)

    if is_num:
        if num == 1:
            print("To start the interactive experiments,"
                  " input a number to determine which opponent algorithm to use.\r\n"
                  "Input non-number other numbers which are not included into this hints "
                  "to exit without running any experiments;\r\n")

            hints = ""
            for i in range(0, supported_experiments_list.__len__()):
                hints += "input {index} to start the experiment {exp_name} interactively;\r\n".format(
                    index=i + 1, exp_name=supported_experiments_list[i])

            experiment = input(hints)
            is_num, exp_num = number_helpers.to_int_tuple(experiment)

            if is_num and supported_experiments_list.__len__() >= exp_num > 0:
                # print("Now start experiment {exp_name} ...... {exp_value} \r\n".format(
                #     exp_name=supported_experiments_list[exp_num - 1],
                #     exp_value=supported_experiments_map[
                #         supported_experiments_list[exp_num - 1]].__str__()))

                tester = InteractiveTester()
                tester.start_test(supported_experiments_map[
                                      supported_experiments_list[exp_num - 1]])
            else:
                pass

        # run automatic tests
        elif num == 0 or is_num:
            print("To start the automatic experiments,"
                  " input a number to determine which algorithm to use in the support list. \r\n"
                  "Input non-number other numbers which are not included into this hints "
                  "to exit without running any experiments;\r\n")

            hints = ""
            for i in range(0, supported_experiments_list.__len__()):
                hints += "input {index} to start the experiment with {exp_name};\r\n".format(
                    index=i + 1, exp_name=supported_experiments_list[i])

            experiment = input(hints)

            is_num, exp_num = number_helpers.to_int_tuple(experiment)

            if is_num and supported_experiments_list.__len__() >= exp_num > 0:

                exp2 = input("Please decide how many sizes should be tested. "
                             "Input 1~5, if you decide run 5 sizes, it will take much time: \r\n")
                is_num, exp2_num = number_helpers.to_int_tuple(exp2)

                if is_num and 1 <= exp2_num <= 5:
                    tester = AutomaticTester(exp2_num)
                    tester.start_test(supported_experiments_map[
                                          supported_experiments_list[exp_num - 1]])
                pass
            else:
                pass

            pass

        else:
            pass

    print("\r\n--------------------------------------------------------\r\nExperiments completed, press ENTER to exit")
    input()
    exit(0)
