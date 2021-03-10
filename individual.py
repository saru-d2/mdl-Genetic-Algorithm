import numpy as np
import config as conf
import random
import secrets
from client import get_errors


class Individual:
    def __init__(self, genes, errorTuple=None):
        # handle mutation
        self.genes = np.copy(genes)
        if errorTuple == None:
            self.genes = mutate(self.genes)
            self.errorTuple = getError(self.genes)
        else:
            self.errorTuple = errorTuple

        self.error = abs(self.errorTuple[0] - self.errorTuple[1]) * (
            self.errorTuple[0] + self.errorTuple[1])
        # penalizing overfitting
        if abs(self.errorTuple[0] - self.errorTuple[1]) >= 200000:
            self.error += 500000


def mutate(genes):
    mutateProb = conf.MUTATE_PROB
    numMutate = conf.NUM_MUTATE
    indsToMutate = np.random.choice(np.arange(0, 11), numMutate, replace=False)

    for index in indsToMutate:
        # if it should be mutated or left alone

        if genes[index] == 0:
            genes[index] = random.uniform(-1e-20, 1e-20)

        if mutateProb >= random.random():
            # mutate!

            genes[index] *= random.uniform(-conf.MUTATE_FACTOR,
                                           conf.MUTATE_FACTOR) + 1
            # make sure weights are btw -10, 10
            genes[index] = min(genes[index], 10.0)
            genes[index] = max(genes[index], -10.0)

    return genes


def getError(genes):
    if conf.TEST:
        return [random.uniform(0, 10000), random.uniform(0, 10000)]
    return get_errors(secrets.KEY, genes.tolist())
