import numpy as np
import config as conf
from individual import Individual

class Population:
    '''object for population'''
    def __init__(self, ch):
        self.popList = []
        if ch == 1:
            # random, initial
            for i in range(conf.POPULATION_SIZE):
                self.popList.append(Individual(conf.OVERFIT, 1, 10))

    def print(self):
        '''prints population'''
        print('----POPULATION----')
        for individual in self.popList:
            print(individual.genes)
            print(individual.error)
        print('')

    def sort(self):

            
def mate(par1, par2):
    ratio = par1.error / (par2.error + par1.error) 
    numFromPar2 = int(ratio * 11)
    numFromPar1 = 11 - numFromPar2
    child1Genes = par1.genes.copy()
    child2Genes = par2.genes.copy()
    indList = np.random.choice(np.arange(0, 11), numFromPar2, replace= False)
    for index in indList:
        child1Genes[index], child2Genes[index] = child2Genes[index], child2Genes[index]

    return child1Genes, child2Genes
