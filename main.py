import config as conf
import numpy as np
import pandas as pd
import colorama
import matplotlib.pyplot as plt
from client import get_errors , get_overfit_vector
from population import Population, newGeneration
import secrets


print('hello world ughhhh')

# ch = int(input('choose: 1. start from scratch'))

ch = 1
Gen1 = Population(ch)
Gen1.sort()
Gen1.print()

# Gen2 = newGeneration(Gen1)
# Gen2.sort()
# Gen2.print()
newGeneration(Gen1)


