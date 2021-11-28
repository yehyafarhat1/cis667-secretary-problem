import csv


def remove(string_input): 
    return "".join(string_input.split()) 


def best_value(cvs_file): #returns the best value in a dataset 
    with open('data/second_testing_set.csv', 'r') as file:
        reader = file.readlines()
        last_row =  remove(reader[-1])
    c = 0
    final = ""
    for i in last_row:
        if i == ",": c += 1
        if c == 2:
            final = final + i
        if i  ==3: break  
    return final[1:] 



def candidate_value(x): #returns the candidate value in a dataset 
    row = remove(x)
    c = 0
    final = ""
    for i in row:
        if i == ",": c += 1
        if c == 1:
            final = final + i
        if i  ==2: break  
    return final[1:] 



    