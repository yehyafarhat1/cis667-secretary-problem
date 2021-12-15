import LSTM
import random
import numpy as np

size = random.randint(2,10)
new_candidates=np.random.choice(11, size, p =[0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.1])

print(new_candidates)


score = new_candidates[0]
v = None
print(score)

for t in range(len(new_candidates)-1):
  x = dictionary[score]
  y, v = net(dictionary[tokens[t]], v)
  y = y.squeeze() # ignore singleton dimensions for time-step/example
  w = y.argmax()
  single_candidate = candidate_score[w]
  prob = y[w]
  print(single_candidate, prob.item())