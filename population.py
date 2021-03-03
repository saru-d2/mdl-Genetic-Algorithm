import numpy as np
import config as conf
from individual import Individual
import random


class Population:
    '''object for population'''

    def __init__(self, popList, genNumber):
        self.popList = []
        self.genNumber = genNumber

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


def crossoverOld(par1, par2):
    # simply exchanging random genes
    child1Genes = par1.genes.copy()
    child2Genes = par2.genes.copy()
    randPrefix = random.randint(0, 11)
    indList = np.arange(0, randPrefix)
    # indList = np.random.choice(np.arange(0, 11), 5, replace=False)
    for index in indList:
        child1Genes[index], child2Genes[index] = child2Genes[index], child2Genes[index]

    return child1Genes, child2Genes


def crossover(par1, par2):
    # fancy, uses simulated binary crossover... keeps avg same, distributes all genes uniformly

    par1genes = par1.genes.copy()
    par2genes = par2.genes.copy()

    u = random.uniform(0, 1)
    
    nc = 3

    if u < 0.5:
        beta = (2 * u) ** (1/(nc+1))
    else:
        beta = (2 * (1 - u)) ** (-1 / (nc+1))

    # nc decides how diff child will be from parent
    # beta is the similarity to the parents AKA spread factor

    child1genes = 0.5 * ((1 + beta) * par1genes + (1 - beta) * par2genes)
    child2genes = 0.5 * ((1 - beta) * par1genes + (1 + beta) * par2genes)

    # ensure that weigths are belong to [-10, 10]
    for i in range(11):
        child1genes[i], child2genes[i] = min(
            child1genes[i], 10), min(child2genes[i], 10)
        child1genes[i], child2genes[i] = max(
            child1genes[i], -10), max(child2genes[i], -10)

    return child1genes, child2genes


def newGeneration(oldgen):
    total_error = 0
    for i in oldgen.popList[:conf.BREEDING_POOL_SIZE]:
        total_error += i.error

    probs = []
    for i in oldgen.popList[:conf.BREEDING_POOL_SIZE]:
        probs.append((total_error - i.error) /
                     (total_error*(conf.BREEDING_POOL_SIZE-1)))
    print(len(probs))

    print(probs)

    print(np.sum(np.array(probs)))

    childGenesList = []
    print('len oldgen.poplist ' + str(len(oldgen.popList)))

    while len(childGenesList) < conf.POPULATION_SIZE:
        # indsToMate = np.random.choice(np.arange(0, conf.POPULATION_SIZE), 2, replace=False, p=probs)
        indsToMate = np.random.choice(
            np.arange(0, conf.BREEDING_POOL_SIZE), 2, replace=False, p=probs)
        print("Selected maties: " + str(indsToMate))
        
        child1Genes, child2Genes = crossover(
            oldgen.popList[indsToMate[0]], oldgen.popList[indsToMate[1]])
        childGenesList.append(Individual(child1Genes))
        childGenesList.append(Individual(child2Genes))
        # childGenesList.append(child1Genes)

    bestofBothGenerations = oldgen.popList[:
                                           conf.NUM_PARENTS_PASSDOWN] + childGenesList
    bestofBothGenerations.sort(key=lambda x: x.error)
    print('---sortedlist-----')
    for i in bestofBothGenerations:
        print(i.error)
    print('-----------------')

    return Population(bestofBothGenerations[0:conf.POPULATION_SIZE], oldgen.genNumber + 1)
