import pickle
import config as conf
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
generations = []

numGens = 10

time = '23-15-29-43'

print(len(sys.argv))
print(sys.argv)

if len(sys.argv) >= 3:
    time = sys.argv[1]
    numGens = int(sys.argv[2])
for i in range(numGens):
    with open('./prevResults/' +time+ '/gen' + str(i+1) + '.pkl', 'rb') as fd:
        generations.append(pickle.load(fd))
avgerr = np.zeros(numGens)
bestErr = np.zeros(numGens)
for idx, gen in enumerate(generations):
    bestErr[idx] =  gen[0][1][0] + gen[0][1][1]
    
    for _, err in gen:
        avgerr[idx] +=  err[1] + err[0]

avgerr /= numGens

print(avgerr)
print(bestErr)

plt.plot(avgerr, label = 'avgErr')
plt.legend()
plt.show()



plt.plot(bestErr, label = 'bestErr')
plt.legend()
plt.show()

bestVector = generations[-1][0][0]
print(bestVector)