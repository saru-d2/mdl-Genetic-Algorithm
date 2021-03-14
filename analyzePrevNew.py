import json
import matplotlib.pyplot as plt
import numpy as np
import config as conf

fileName = 'MAR14NEW.json'
with open(fileName) as fd:
    data = json.load(fd)

numGens = len(data['PrevGens'])
print(numGens)
avgErr = np.array([])
bestErr = np.array([])


for gen in data['PrevGens']:
    bestErr = np.append(
        bestErr, gen['popList'][0]['errorTuple'][0] + gen['popList'][0]['errorTuple'][1])
    curArr = []
    avgErr = np.append(avgErr, 0)
    for i in gen['popList']:
        # print( i['errorTuple'])
        avgErr[-1] += i['errorTuple'][0] + i['errorTuple'][1]
    avgErr[-1] /= conf.POPULATION_SIZE

print(avgErr)
print(bestErr)

plt.plot(avgErr, label='avgErr')
plt.legend()
plt.show()


plt.plot(bestErr, label='bestErr')
plt.legend()
plt.show()


bestVector = data['PrevGens'][-1]['popList'][0]['genes']
print(np.format_float_scientific(data['PrevGens'][-1]['popList'][0]['errorTuple'][0]))
print(np.format_float_scientific(data['PrevGens'][-1]['popList'][0]['errorTuple'][1]))
print('best')
print(bestVector)


# [13510723304.19212, 368296592820.6967]