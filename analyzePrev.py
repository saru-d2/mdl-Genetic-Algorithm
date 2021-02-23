import pickle
import config as conf
import numpy as np
import matplotlib.pyplot as plt

generations = []

numGens = 10
time = '23-15-29-43'

for i in range(numGens):
    with open('./prevResults/' +time+ '/gen' + str(i+1) + '.pkl', 'rb') as fd:
        generations.append(pickle.load(fd))
avgerr = np.zeros(numGens)
bestErr = np.zeros(numGens)
for idx, gen in enumerate(generations):
    bestErr[idx] =  gen[0][1][1]
    for _, err in gen:
        avgerr[idx] +=  err[1]

avgerr /= numGens

plt.plot(avgerr, label = 'avgErr')
plt.legend()
plt.show()

print(avgerr)
print(bestErr)


plt.plot(bestErr, label = 'bestErr')
plt.legend()
plt.show()