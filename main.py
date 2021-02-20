import config as conf
import numpy as np
import pandas as pd
from population import Population, newGeneration
import secrets
import pickle
from datetime import datetime
import utilities


print('hello world ughhhh')

# ch = int(input('choose: 1. start from scratch'))


generations = []

ch = 1
init = Population(ch)
init.print()
generations.append(init)
utilities.print_stats(generations[0], 1)
utilities.pickleDump(generations[0], 1)

for curgenNum in range(2, 5):
    pregen = generations[-1]
    curgen = newGeneration(pregen)
    generations.append(curgen)
    utilities.pickleDump(curgen, curgenNum)
    # print(curgen.getFittest().error)
    utilities.print_stats(generations[curgenNum - 1], curgenNum)

