import config as conf
import numpy as np
import pandas as pd
from population import Population, newGeneration
import secrets
import pickle
from datetime import datetime
import matplotlib.pyplot as plt
import utilities


print('hello world ughhhh')

# ch = int(input('choose: 1. start from scratch'))


generations = []
avg_errs = []
least_errs = []

ch = 1
init = Population(ch)
init.print()
generations.append(init)
utilities.print_stats(generations[0], 1)
utilities.pickleDump(generations[0], 1)
avg_errs.append(generations[-1].getMeanError())
least_errs.append(generations[-1].getFittest().error)

for i in range(1, conf.NUM_GENS):
    curgenNum = i + 1
    pregen = generations[-1]
    curgen = newGeneration(pregen)
    generations.append(curgen)
    utilities.pickleDump(curgen, curgenNum)
    # print(curgen.getFittest().error)
    utilities.print_stats(generations[curgenNum - 1], curgenNum)
    avg_errs.append(generations[-1].getMeanError())
    least_errs.append(generations[-1].getFittest().error)


plt.plot(range(1, conf.NUM_GENS + 1), least_errs, label='best')
plt.plot(range(1, conf.NUM_GENS + 1), avg_errs, label='avg')
plt.legend()
plt.show()
