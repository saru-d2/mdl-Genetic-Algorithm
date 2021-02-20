
import pickle

generations = []

numGens = 4
time = '21-02-02-07'

for i in range(numGens):
    with open('./prevResults/' +time+ 'gen' + str(i+1) + '.pkl', 'rb') as fd:
        generations.append(pickle.load(fd))

objs = []

for idx, population in enumerate(generations):
    genNo = idx + 1
    print('\n\n\n')
    for Individual, err in population:
        print(err)
    