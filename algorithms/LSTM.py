import random
import numpy as np
import torch as tr

population = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
weights = [0.05, 0.1, 0.05, 0.1, 0.3, 0.0, 0.1, 0.1, 0.1, 0.1]

candidates = []

for i in range(10):
    size = random.randint(2, 10)
    n = np.random.choice(11, 20, p=[0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.1])
    candidates.append(n)

candidate_score = set()
for z in candidates:
    for j in z:
        candidate_score.add(j)
candidate_score = tuple(candidate_score)  # deterministic order

I = tr.eye(len(candidate_score))
dictionary = {
    word: I[w].reshape(1, 1, len(candidate_score))
    for w, word in enumerate(candidate_score)}


# Define a small LSTM recurrent neural network with linear hidden-to-output layer
class Net(tr.nn.Module):
    def __init__(self, hidden_size):
        super(Net, self).__init__()
        self.lstm = tr.nn.LSTM(input_size=len(candidate_score), hidden_size=hidden_size)
        self.readout = tr.nn.Linear(in_features=hidden_size, out_features=len(candidate_score))

    def forward(self, x, v=None):
        _, v = self.lstm(x) if v is None else self.lstm(x, v)  # update hidden from input
        h, c = v  # LSTM hidden vector and internal so-called "cell state"
        y = self.readout(h)  # get output from hidden
        y = tr.softmax(y, dim=-1)  # make sure output is a probability distribution
        return y, v


net = Net(3)
opt = tr.optim.SGD(net.parameters(), lr=0.01)

for epoch in range(2000):

    batch_loss = 0.

    for scores in candidates:
        tokens = scores

        v = None  # no hidden activation at first time-step
        for t in range(len(tokens) - 1):
            y, v = net(dictionary[tokens[t]], v)
            y_target = dictionary[tokens[t + 1]]

            # loss = tr.sum((y - y_target)**2) # MSE
            loss = -tr.sum(y_target * tr.log(y))  # Cross-entropy
            batch_loss += loss

    batch_loss.backward()
    opt.step()
    opt.zero_grad()

    # if epoch % 100 == 0: print(epoch, batch_loss.item())

size = random.randint(2, 10)
new_candidates = np.random.choice(11, size, p=[0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05, 0.1])

print(new_candidates)

score = new_candidates[0]
v = None
print(score)

for t in range(len(new_candidates) - 1):
    x = dictionary[score]
    y, v = net(dictionary[tokens[t]], v)
    y = y.squeeze()  # ignore singleton dimensions for time-step/example
    w = y.argmax()
    single_candidate = candidate_score[w]
    prob = y[w]
    print(single_candidate, prob.item())
