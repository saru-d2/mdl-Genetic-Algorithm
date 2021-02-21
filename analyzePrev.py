
import pickle
import config as conf
import numpy as np
import matplotlib.pyplot as plt

generations = []

numGens = 10
time = '21-21-57-54'

for i in range(numGens):
    with open('./prevResults/' +time+ '/gen' + str(i+1) + '.pkl', 'rb') as fd:
        generations.append(pickle.load(fd))

objs = []


bestTrainErr = np.array([])
avgTrainErr = np.array([])
bestTestErr = np.array([])
avgTestErr = np.array([])
    
for gen in generations:
    totTrainErr = 0
    minTrainErr = np.inf

    totTestErr = 0
    minTestErr = np.inf

    for Individual, err in gen:
        print(err)
        minTrainErr = min(minTrainErr,   err[0])
        totTrainErr +=  err[0] 

        minTestErr = min(minTestErr,   err[1])
        totTestErr +=  err[1] 

    bestTrainErr = np.append(bestTrainErr, minTrainErr)
    avgTrainErr = np.append(avgTrainErr, totTrainErr / conf.POPULATION_SIZE)

    bestTestErr = np.append(bestTestErr, minTestErr)
    avgTestErr = np.append(avgTestErr, totTestErr / conf.POPULATION_SIZE)
    print('')


# plt.plot(avgErr)
# plt.plot(bestTestErr + bestTrainErr, label='bestError')
plt.plot(bestTestErr , label='bestTest')
plt.plot(bestTrainErr, label='bestTrain')
plt.legend()
plt.show()

plt.plot(avgTestErr + avgTrainErr, label='avgError')
plt.plot(avgTestErr , label='avgTest')
plt.plot(avgTrainErr, label='avgTrain')
plt.legend()
plt.show()