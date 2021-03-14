import numpy as np
import random

from population import Population, newGeneration
from individual import Individual
import config as conf
import utils


print('hello world ughhhh')

# ch = int(input('choose: 1. start from scratch'))

generations = []

startGenNum = 1

if utils.prevDataExists():
    prevData = utils.loadPrevData()
    prevData = prevData['PrevGens']
    prevPopList = []
    lastGen = prevData[-1]
    for each in lastGen['popList']:
        prevPopList.append(Individual(each['genes'], each['errorTuple']))
    initPopulation = Population(prevPopList, lastGen['genNumber'])
    startGenNum = lastGen['genNumber']

else:
    initPopList = []
    for i in range(conf.POPULATION_SIZE):
        curGene = conf.OVERFIT.copy()
        # it chooses random features to ignore
        initPopList.append(Individual(curGene))
        print(curGene)
    initPopulation = Population(initPopList, 1)
    print(initPopulation.popList)
    utils.writeJSON(initPopulation)


generations.append(initPopulation)
utils.print_stats(generations[0], 1)

avgErr = []
bestErr = []

for i in range(1, conf.NUM_GENS):
    curgenNum = startGenNum + i
    pregen = generations[-1]
    curgen = newGeneration(pregen)
    generations.append(curgen)
    avgErr.append(generations[-1].getMeanError())
    bestErr.append(generations[-1].getFittest().error)
    utils.appendGenToFile(curgen)
    
    
    print(curgen.getFittest().errorTuple[0])
    print(curgen.getFittest().errorTuple[1])
    print(curgen.getFittest().genes)
    inp = input('continue?')
    if inp == 'NO':
        break

    


print(bestErr)

print(avgErr)

# generations[-1].getFittest().submit()
