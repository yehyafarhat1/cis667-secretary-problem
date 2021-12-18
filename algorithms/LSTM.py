import random
import numpy as np
import torch as tr
import math

population = [0, 1, 2, 3, 4, 5,6,7,8,9]
weights = [0.05, 0.1, 0.05, 0.1, 0.3, 0.0, 0.1, 0.1, 0.1, 0.1]



candidates = []

for i in range(25):
    n=np.random.choice(11, 20, p =[0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.1])
    candidates.append(n)
    


candidate_score = set()
for z in candidates:
  for j in z:
    candidate_score.add(j)
candidate_score = tuple(candidate_score) # deterministic order


I = tr.eye(len(candidate_score))
dictionary = {
    score: I[w].reshape(1,1,len(candidate_score))
    for w,score in enumerate(candidate_score)}


# Define a small LSTM recurrent neural network with linear hidden-to-output layer
class Net(tr.nn.Module):
  def __init__(self, hidden_size):
    super(Net, self).__init__()
    self.lstm = tr.nn.LSTM(input_size = len(candidate_score), hidden_size = hidden_size)
    self.readout = tr.nn.Linear(in_features=hidden_size, out_features=len(candidate_score))
  def forward(self, x, v=None):
    _, v = self.lstm(x) if v is None else self.lstm(x, v) # update hidden from input
    h, c = v # LSTM hidden vector and internal so-called "cell state"
    y = self.readout(h) # get output from hidden
    y = tr.softmax(y, dim=-1) # make sure output is a probability distribution
    return y, v

net = Net(3)
opt = tr.optim.SGD(net.parameters(), lr=0.01)

for epoch in range(2000):

  batch_loss = 0.

  for scores in candidates:
    tokens = scores

    v = None # no hidden activation at first time-step
    for t in range(len(tokens)-1):

      y, v = net(dictionary[tokens[t]], v)
      y_target = dictionary[tokens[t+1]]

      #loss = tr.sum((y - y_target)**2) # MSE
      loss = -tr.sum(y_target * tr.log(y)) # Cross-entropy
      batch_loss += loss

  batch_loss.backward()
  opt.step()
  opt.zero_grad()

  if epoch % 100 == 0: print(epoch, batch_loss.item())
  
  




# Initial hidden state will default to zeros
v = None


def predict_list(candidate_list):  # this function will predict the number of candidates we will get, this is purely based on the LSTM. only the first real value is given to the model all other values are based on the predictions regardless if they are right or wrong 
  predicted_lst = []
  
  v = None
  if candidate_list[0] == 0:
    return predicted_lst
  x = dictionary[candidate_list[0]]
  y, v = net(x, v)
  y = y.squeeze() 
  w = y.argmax()
  score = candidate_score[w]
  prob = y[w]
  i = 0
 
  while (score != 0):
    i += 1
    if i == 21:
      break
    x = dictionary[score]
    y, v = net(x, v)
    y = y.squeeze()
    w = y.argmax()
    score = candidate_score[w]
    prob = y[w]
    t = (score,prob.item())
    
    
    predicted_lst.append(t)
  return predicted_lst



def make_decision(candidate_lst):                             
  lstm_prediction_lst_length = len(predict_list(candidate_lst)) # this is the list lstm predicts, this is based only on the first real value of the candidates while all other predictions are based on lstm 
  #lstm_prediction_lst_length =0
  # we will now try to apply the 37% rule according to our predicted length of the list, it will always be 20 unless the lstm model predicts a 0 before we get to a length of 20 then in that case it will be shorter
  # we will reject the first  length(lstm_prediction_lst)/ e candidates 
  print(lstm_prediction_lst_length)
  
  if lstm_prediction_lst_length == 0:  #this is a corner case where lstm predicts that we will not get any candidates, if we get one accept the first one that arrives 
     if candidate_lst[0] == 0:
       print("did not get any candidates")
       return 0
     else:
       print("lstm predicted that we will not get any candidates, we ended up getting one and immediately accepted")
       return candidate_lst[0]



  reject = math.floor(lstm_prediction_lst_length)
  
  v = None
  max = -1
  for i in range(reject):
   

    if candidate_lst[i] ==0:
      print("lstm miscalculation, number of candidates predicted by lstm was bigger than what we actaully got. rejected all candidates")
      return 0,i #-------------------------------------
       #this means that our lstm model has made a miscalculation that we will get further candidate. if we get a 0 then that means we rejected our last candidate and didnt get anymore so we end up with no candidate 

    if candidate_lst[i] > max: max = candidate_lst[i]

    x = dictionary[candidate_lst[i]]
    y, v = net(x, v)
    y = y.squeeze() 
    w = y.argmax()
    score = candidate_score[w]
    prob = y[w]
    
    
    if score == 0:                      #---------------------------
      if prob.item() > 0.1:
        print("high probability of no candidates, take current option")
        return candidate_lst[i], i #if the lstm model predicts that there is a high probability of 0 (not get getting anymore candidates) then abandon the plan and take whatever candidate we have now
      else:pass                                   #otherwise continue with the 37% rule calculations


  remaining_candidates = candidate_lst[reject:]
  v =None

  for j in range(len(remaining_candidates)):
    if remaining_candidates[j] ==0:
      print("no candidates left after rejecting first 37%") 
      return 0,j+reject #-----------------------------------------
                                                            #--------------------------------------------------
    if remaining_candidates[j] > max:
      print("37% applied properly using the predicted length of the list")
      return remaining_candidates[j],j+reject # this means we have succesfully applied the 37% rule
    else:
      x = dictionary[candidate_lst[j]]
      y, v = net(x, v)
      y = y.squeeze() 
      w = y.argmax()
      score = candidate_score[w]
      prob = y[w]
      if score == 0:                          #-----------------------------------------------
        if prob.item() > 0.1:
          print("high probability of no candidates, take current option")
          return candidate_lst[j], j+reject # same as before, before we reject the candidate and move on we predict the next value. if the model predicts with a high probability that we will not get anymore candidates abandon the task and take whatever we have now
    

  #if both these loops do not return a value then that means our best candidates were contained in the first 37% and we reject all of them. since the length of the list represents the timeframe we want to hire someone in we just take the last candidate and we can disregard the possibility of an infinite time frame
  print("allocated time frame to choose candidate is done, pick final candidate before due date")
  return candidate_lst[len(candidate_lst)-1], len(candidate_lst)-1


for i in range(500):
  new_candidates=np.random.choice(11, 20, p =[0.1, 0.1, 0.05, 0.2, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1])
  print(make_decision(new_candidates))