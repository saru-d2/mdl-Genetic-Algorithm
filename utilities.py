import pickle
from datetime import datetime
from population import Population
from individual import Individual
import os

curDateTime = datetime.now().strftime("%d-%H-%M-%S")


def pickleDump(population, gen):
    indiList = []
    for individual in population.popList:
        indiList.append([individual.genes, individual.errorTuple])
    os.makedirs(os.path.dirname('./prevResults/' + curDateTime +
                                '/gen' + str(gen) + '.pkl'), exist_ok=True)
    with open('./prevResults/' + curDateTime + '/gen' + str(gen) + '.pkl', 'xb') as fd:
        pickle.dump(indiList, fd)


def print_stats(population, gen):
    print('gen ' + str(gen))
    print('avg ' + str(population.getMeanError()))
    print('best ' + str(population.getFittest().error))
