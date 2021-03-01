import utils
import matplotlib.pyplot as plt
import numpy as np
import config as conf

data = utils.loadPrevData()

numGens = len(data['PrevGens'])
print(numGens)
avgErr = np.array([])
bestErr = np.array([])


for gen in data['PrevGens']:
    bestErr = np.append(
        bestErr, gen['popList'][0]['errorTuple'][0] + gen['popList'][0]['errorTuple'][1])
    avgErr = np.append(avgErr, [0, 0])
    for i in gen['popList']:
        # print( i['errorTuple'])
        avgErr[-1] += gen['popList'][0]['errorTuple'][0] + \
            gen['popList'][0]['errorTuple'][1]
    avgErr /= conf.POPULATION_SIZE

plt.plot(avgErr, label='avgErr')
plt.legend()
plt.show()


plt.plot(bestErr, label='bestErr')
plt.legend()
plt.show()
