
import pickle

generations = []

numGens = 4
time = '21-01-56-25'

for i in range(numGens):
    with open('./prevResults/' +time+ 'gen' + str(i+1) + '.pkl', 'rb') as fd:
        generations.append(pickle.load(fd))

objs = []

for idx, population in enumerate(generations):
    genNo = idx + 1
    
    for Individual in population:
        print('')
        print(Individual)
    