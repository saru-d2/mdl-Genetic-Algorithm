import numpy as np
import config as conf
from individual import Individual

class Population:
    '''object for population'''
    def __init__(self, ch, genesList=None):
        self.popList = []
        if ch == 1:
            # random, initial
            for i in range(conf.POPULATION_SIZE):
                self.popList.append(Individual(conf.OVERFIT, 1, 10))
        elif ch == 2:
            for genes in genesList:
                self.popList.append(Individual(genes, 1, 10))


    def print(self):
        '''prints population'''
        print('----POPULATION----')
        for individual in self.popList:
            print(individual.genes)
            print(individual.error)
        print('')

    def sort(self):
        self.popList.sort(key=lambda x : x.error)


            
def crossover(par1, par2):
    child1Genes = par1.genes.copy()
    child2Genes = par2.genes.copy()
    indList = np.random.choice(np.arange(0, 11), 5, replace= False)
    for index in indList:
        child1Genes[index], child2Genes[index] = child2Genes[index], child2Genes[index]

    return child1Genes, child2Genes

def newGeneration(oldgen):
    oldgen.sort()
    total_error = 0
    for i in oldgen.popList:
        total_error += i.error
    total_error

    probs = []
    for i in oldgen.popList:
        probs.append((total_error - i.error) /(total_error*(conf.POPULATION_SIZE-1)))

    print(probs)

    print(np.sum(np.array(probs)))
    
    genesList=[]

    for i in range(conf.POPULATION_SIZE//2):
        indsToMate = np.random.choice(np.arange(0, conf.POPULATION_SIZE), 2, replace=False, p=probs)
        print("Selected maties: " + str(indsToMate))
        # child1Genes, child2Genes = crossover(
        #     oldgen.popList[indsToMate[0]], oldgen.popList[indsToMate[1]])
        # genesList.append(child1Genes)
        # genesList.append(child2Genes)

    # return Population(2,genesList)