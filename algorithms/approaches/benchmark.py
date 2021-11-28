import csv
import numpy as np
import matplotlib.pyplot  as plt

def remove(string_input): 
    return "".join(string_input.split()) 

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




def choose_candidate(x):
    with open('data/{}_testing_set.csv'.format(x), 'r') as file:
        c = file.readlines() 

    

    cv = list(map(candidate_value,c))
    candidate_values = list(map(float,cv[1:]))

    n = len(candidate_values)
    
    stop = int(round(n/np.e))
    
    best_from_rejected = np.max(candidate_values[:stop])
    rest = candidate_values[stop:]

    chosen_candidate =0
    for i in rest:
        if i > best_from_rejected:
            chosen_candidate = i
            break
        else:
            chosen_candidate = candidate_values[-1]
    
    return chosen_candidate
        
        
# choose from 100 candidates and run simulation 100,000 times
sim = np.array([choose_candidate('first'),choose_candidate('second'),choose_candidate('third'),choose_candidate('fourth'),choose_candidate('fifth')])


plt.figure(figsize=(10, 6))
plt.hist(sim, bins=100)
plt.xticks(np.arange(0, 101, 10))
plt.ylim(0, 4)
plt.xlabel('Chosen candidate')
plt.ylabel('frequency')
plt.show()
    
    
plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(np.histogram(sim, bins=100)[0])/5)
plt.ylim(0,1)
plt.xlim(0, 100)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xticks(np.arange(0, 101, 10))
plt.xlabel('Chosen candidate')
plt.ylabel('Cumulative probability')
plt.show()


