import csv
import copy
import os

import number_helpers
from algorithms.prime_37percent import Prime_37percent

COL_Candidate_Index = "Candidate Index"
COL_Candidate_Value = "Candidate Value"
COL_Current_Best_Candidate_Value = "Current Best Candidate Value"
COL_Current_Best_Candidate_Index = "Current Best Candidate Index"

instance_a = Prime_37percent()

supported_experiments_list = []
supported_experiments_map = {}
# TODO: Add all the experiment models here
# supported_experiments_list.append("Experiment A")
# supported_experiments_map["Experiment A"] = "This is A"
# supported_experiments_list.append("Experiment B")
# supported_experiments_map["Experiment B"] = "This is B"
# supported_experiments_list.append("Experiment C")
# supported_experiments_map["Experiment C"] = "This is C"
supported_experiments_list.append(instance_a.name())
supported_experiments_map[instance_a.name()] = instance_a


def read_preset_data(filename):
    data_list = []
    path_str = os.path.join("data", filename)
    if os.path.exists(path_str):
        with open(path_str, encoding="utf-8", mode='r') as csvFile:
            readCSV = csv.reader(csvFile)
            # skip header
            next(readCSV)
            # Candidate Index, Candidate Value, Current Best Candidate Value, Current Best Candidate Index
            for row in readCSV:
                col1 = int(row[0])
                col2 = float(row[1])
                col3 = float(row[2])
                col4 = int(row[3])
                data_list.append({COL_Candidate_Index: col1,
                                  COL_Candidate_Value: col2,
                                  COL_Current_Best_Candidate_Value: col3,
                                  COL_Current_Best_Candidate_Index: col4})

    return data_list


def write_one_row_format(is_selected, best_at_present, best_value_at_present, csv_row_dict):
    print("Current:{index}; \t\t Value:{value}; \t Selected: {is_selected};"
          " \t Best index now {best_at_present}; \t\t Best value now {best_value_at_present};"
          " \t Optimal Value {optimal} \r\n".format(
        index=csv_row_dict[COL_Candidate_Index].__str__().rjust(5, ' '),
        value=csv_row_dict[COL_Candidate_Value].__str__().rjust(5, ' '),
        is_selected=is_selected,
        best_at_present=best_at_present, best_value_at_present=best_value_at_present.__str__().rjust(5, ' '),
        optimal=csv_row_dict[COL_Current_Best_Candidate_Value].__str__().rjust(5, ' ')
    ))


def compare_and_result(csv_data):
    print('--------------------------------------------------------------------------------------------------------')
    print('========================================================================================================')
    pass


def run_one_dataset(model, csv_data):
    model_instance = copy.deepcopy(model)
    for i in range(0, len(csv_data)):
        is_selected, best_at_present = model_instance.decide(i, csv_data[i][COL_Candidate_Value])
        csv_data[i]["Is Selected"] = is_selected
        csv_data[i]["Model Best at present"] = best_at_present
        csv_data[i]["Model Best Value at present"] = \
            csv_data[best_at_present][COL_Candidate_Value] if best_at_present >= 0 else 0
        write_one_row_format(is_selected, best_at_present,
                             csv_data[i]["Model Best Value at present"], csv_data[i])
    compare_and_result(csv_data)


if __name__ == "__main__":
    strategy = input("To start the test case, input a number to determine which strategy to use.\r\n"
                     "Input non-number other numbers which are not included into this hints "
                     "to exit without running any experiments;\r\n"
                     "input 0 or other non-digit to start all the pre-set experiments automatically;\r\n"
                     "input 1 to start interactive experiments;\r\n"
                     "input 2 to run an experiment separately. ")  # Python 3
    # raw_input("......")  # Python 2

    is_num, num = number_helpers.to_int_tuple(strategy)

    if is_num:
        if num == 1:
            print("To start the interactive experiments,"
                  " input a number to determine which experiment to use.\r\n"
                  "Input non-number other numbers which are not included into this hints "
                  "to exit without running any experiments;\r\n")

            hints = ""
            for i in range(0, supported_experiments_list.__len__()):
                hints += "input {index} to start the experiment {exp_name} interactively;\r\n".format(
                    index=i + 1, exp_name=supported_experiments_list[i])

            experiment = input(hints)
            is_num, exp_num = number_helpers.to_int_tuple(experiment)

            if is_num and supported_experiments_list.__len__() >= exp_num > 0:
                print("Now start experiment {exp_name} ...... {exp_value} \r\n".format(
                    exp_name=supported_experiments_list[exp_num - 1],
                    exp_value=supported_experiments_map[
                        supported_experiments_list[exp_num - 1]].__str__()))

            else:
                pass

        elif num == 2:
            print("To start the automatic experiments,"
                  " input a number to determine which experiment to use.\r\n"
                  "Input non-number other numbers which are not included into this hints "
                  "to exit without running any experiments;\r\n")

            hints = ""
            for i in range(0, supported_experiments_list.__len__()):
                hints += "input {index} to start the experiment {exp_name} interactively;\r\n".format(
                    index=i + 1, exp_name=supported_experiments_list[i])

            experiment = input(hints)

            is_num, exp_num = number_helpers.to_int_tuple(experiment)

            if is_num and supported_experiments_list.__len__() >= exp_num > 0:
                print("Now start experiment {exp_name} ...... {exp_value} \r\n".format(
                    exp_name=supported_experiments_list[exp_num - 1],
                    exp_value=supported_experiments_map[supported_experiments_list[exp_num - 1]]))

                model = supported_experiments_map[supported_experiments_list[exp_num - 1]]

                print("First testing set\r\n")
                csv_data = read_preset_data("first_testing_set.csv")
                run_one_dataset(model, csv_data)

                print("Second testing set\r\n")
                csv_data = read_preset_data("second_testing_set.csv")
                run_one_dataset(model, csv_data)

                print("Third testing set\r\n")
                csv_data = read_preset_data("third_testing_set.csv")
                run_one_dataset(model, csv_data)

                print("Fourth testing set\r\n")
                csv_data = read_preset_data("fourth_testing_set.csv")
                run_one_dataset(model, csv_data)

                print("Fifth testing set\r\n")
                csv_data = read_preset_data("fifth_testing_set.csv")
                run_one_dataset(model, csv_data)

                pass
            else:
                pass
            pass
        else:
            pass

    print("\r\n--------------------------------------------------------\r\nExperiments completed, press ENTER to exit")
    input()
    exit(0)
