import number_helpers

supported_experiments_list = []
supported_experiments_map = {}
# TODO: Add all the experiment models here
supported_experiments_list.append("Experiment A")
supported_experiments_map["Experiment A"] = "This is A"
supported_experiments_list.append("Experiment B")
supported_experiments_map["Experiment B"] = "This is B"
supported_experiments_list.append("Experiment C")
supported_experiments_map["Experiment C"] = "This is C"

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
                      exp_value=supported_experiments_map[supported_experiments_list[exp_num - 1]]))
                pass
            else:
                pass

        elif num == 2:
            pass
        else:
            pass

    print("\r\n--------------------------------------------------------\r\nExperiments completed, press ENTER to exit")
    input()
    exit(0)
