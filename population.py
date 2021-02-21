import numpy as np
import config as conf
from individual import Individual


class Population:
    '''object for population'''

    def __init__(self, ch, popList = None):
        self.popList = []
        if ch == 1:
            # random, initial
            for i in range(conf.POPULATION_SIZE):
                self.popList.append(Individual(conf.OVERFIT, conf.MUTATE_PROB, conf.NUM_MUTATE))
        elif ch == 2:
            # create population from gene
            print(len(popList))
            self.popList = popList

        self.sort()

    def print(self):
        '''prints population'''
        print('----POPULATION----')
        for individual in self.popList:
            print(individual.genes)
            print(individual.error)
        print('')

    def sort(self):
        self.popList.sort(key=lambda x: x.error)

    def getFittest(self):
        return self.popList[0]

    def getMeanError(self):
        errs = []
        for genes in self.popList:
            errs.append(genes.error)
        return np.mean(np.array(errs))


def crossover(par1, par2):
    child1Genes = par1.genes.copy()
    child2Genes = par2.genes.copy()
    indList = np.random.choice(np.arange(0, 11), 5, replace=False)
    for index in indList:
        child1Genes[index], child2Genes[index] = child2Genes[index], child2Genes[index]

    return child1Genes, child2Genes


def newGeneration(oldgen):
    total_error = 0
    for i in oldgen.popList[:conf.BREEDING_POOL_SIZE]:
        total_error += i.error

    probs = []
    for i in oldgen.popList[:conf.BREEDING_POOL_SIZE]:
        probs.append((total_error - i.error) /
                     (total_error*(conf.BREEDING_POOL_SIZE-1)))

    print(probs)

    print(np.sum(np.array(probs)))

    childGenesList = []
    print( 'len oldgen.poplist ' + str(len(oldgen.popList)))

    while len(childGenesList) < conf.POPULATION_SIZE:
        # indsToMate = np.random.choice(np.arange(0, conf.POPULATION_SIZE), 2, replace=False, p=probs)
        indsToMate = np.random.choice(
            np.arange(0, conf.BREEDING_POOL_SIZE), 2, replace=False, p = probs)
        print("Selected maties: " + str(indsToMate))
        child1Genes, child2Genes = crossover(
            oldgen.popList[indsToMate[0]], oldgen.popList[indsToMate[1]])
        childGenesList.append(Individual(child1Genes, conf.MUTATE_PROB, conf.NUM_MUTATE))
        childGenesList.append(Individual(child2Genes, conf.MUTATE_PROB, conf.NUM_MUTATE))
        # childGenesList.append(child1Genes)

    bestofBothGenerations = oldgen.popList + childGenesList
    bestofBothGenerations.sort(key=lambda x: x.error)
    print('---sortedlist-----')
    for i in bestofBothGenerations:
        print(i.error)

    print('-----------------')


    return Population(2, bestofBothGenerations[0:conf.POPULATION_SIZE])