import numpy as np
import config as conf
import random
import secrets
from client import get_errors

class Individual:
    def __init__(self, genes, mutateProb, numMutate):
        # handle mutation
        genes = np.copy(genes)
        self.genes = mutate(genes, mutateProb, numMutate)
        self.errorTuple = getError(self.genes) 
        self.error = (self.errorTuple[0] + self.errorTuple[1]) / 2
        
        #penalizing overfitting
        if abs(self.errorTuple[0] - self.errorTuple[1]) >= 200000:
            self.errorTuple += 200000


def mutate(genes, mutateProb, numMutate):
    indsToMutate = np.random.choice(np.arange(0, 11), numMutate, replace= False)

    for index in indsToMutate:
        # if it should be mutated or left alone

        if mutateProb > random.random():
            #mutate!

            if genes[index] == 0.0:
                genes[index] += random.uniform(-1e-20, 1e-20)

            genes[index] *= random.uniform(-conf.MUTATE_FACTOR, conf.MUTATE_FACTOR ) + 1
            genes[index] = min(genes[index], 10.0)
            genes[index] = max(genes[index], -10.0)

    return genes

def getError(genes):
    return get_errors(secrets.KEY, genes.tolist())