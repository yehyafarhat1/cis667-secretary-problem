import csv
import copy
import os
import random

from algorithms import domain_impl


def to_int_tuple(input_str):
    if input_str is not None:
        num_str = input_str.strip()
        if num_str.isnumeric() or num_str.isdigit():
            int_num = int(num_str)
            return True, int_num

        # only if isnumeric and isdigit couldn't figure out whether it's a number
        # then try the approach which may cause an exception
        # to relieve performance reduction caused by the exception stack
        try:
            num = int(num_str)
            return True, num
        except:
            pass

    return False, -1


def to_float_tuple(input_str):
    if input_str is not None:
        num_str = input_str.strip()
        if num_str.isnumeric() or num_str.isdigit():
            float_num = float(num_str)
            return True, float_num

        # only if isnumeric and isdigit couldn't figure out whether it's a number
        # then try the approach which may cause an exception
        # to relieve performance reduction caused by the exception stack
        try:
            num = float(num_str)
            return True, num
        except:
            pass

    return False, -1.0


def augment_sentences(input_path, size=1000, maxlength=100):
    result_list = []

    # read csv and augment 1000(can be changed by parameter value) random segments
    if os.path.exists(input_path):
        data_list = []
        # read all and close file
        with open(input_path, encoding="utf-8", mode='r') as csvFile:

            readCSV = csv.reader(csvFile)
            # skip header
            next(readCSV)
            # Candidate Index, Candidate Value, Current Best Candidate Value, Current Best Candidate Index
            for row in readCSV:
                col1 = int(row[0])
                col2 = float(row[1])
                col3 = float(row[2])
                col4 = int(row[3])
                data_list.append({domain_impl.COL_Candidate_Index: col1,
                                  domain_impl.COL_Candidate_Value: col2,
                                  domain_impl.COL_Current_Best_Candidate_Value: col3,
                                  domain_impl.COL_Current_Best_Candidate_Index: col4})

        # random n size segments
        for i in range(0, size):
            a = random.randint(0, len(data_list))
            b = random.randint(0, len(data_list))
            while (a >= 0 and b >= 0 and b == a):
                # random until segment exists
                a = random.randint(0, len(data_list))
                b = random.randint(0, len(data_list))

            if a >= 0 and b >= 0:
                if a > b:
                    # swap
                    c = b
                    b = a
                    a = c

                    # slice one piece segment
                new_list = data_list[a:b]
                if len(new_list) > maxlength:
                    new_list = new_list[:maxlength]
                new_list_sentence = []

                for item in new_list:
                    # round the value, then it can reduce the search nodes count
                    item_word = str(round(item[domain_impl.COL_Candidate_Value]/10.0))
                    new_list_sentence.append(item_word)

                new_list_sentence.append('-1')  # terminal as EOF
                result_list.append(new_list_sentence)
                if i % 100 == 99:
                    print('file {file} {count} sentences added'.format(file={input_path}, count=i + 1))

    return result_list
