import config as conf
import numpy as np
import pandas as pd
from population import Population, newGeneration
import secrets
from datetime import datetime
import matplotlib.pyplot as plt
import utils
from individual import Individual
import random


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
        curGene = conf.OVERFIT
        randIndices = np.random.choice(np.arange(0, 11), random.randint(0, 5), replace=False)
        for ind in randIndices:
            curGene[ind] = 0.0
        initPopList.append(Individual(curGene))
    initPopulation = Population(initPopList, 1)
    print(initPopulation.popList)
    utils.writeJSON(initPopulation)
    


generations.append(initPopulation)
utils.print_stats(generations[0], 1)

for i in range(1, conf.NUM_GENS):
    curgenNum = startGenNum + i
    pregen = generations[-1]
    curgen = newGeneration(pregen)
    generations.append(curgen)
    
    utils.appendGenToFile(curgen)



