import json
import matplotlib.pyplot as plt
import numpy as np
import config as conf
import math as meth



class ind:
    def __init__(self, genes, errTuple, gen):
        self.genes = genes
        self.errorTuple = errTuple
        self.gen = gen
        self.error = self.errorTuple[0] + self.errorTuple[1]

def sortAndDedup(indList):
    # indListSet  = set(indList)
    # print(indListSet)
    indList.sort(key=lambda x: x.error)
    indListSet = []
    for i, ind in enumerate(indList):
        if len(indListSet) > 0 and indListSet[-1].genes == ind.genes:
            continue
        indListSet.append(ind)
    return indListSet


fileName = 'prevGensNewNew.json'
with open(fileName) as fd:
    data = json.load(fd)

indList = []

for gen in data['PrevGens']:
    for indFromGen in gen['popList']: 
        #create ind object
        indList.append(ind(indFromGen['genes'], indFromGen['errorTuple'], gen['genNumber']))

indlist2 = sortAndDedup(indList)

best10 = []

for i, ind in enumerate(indlist2):
    # print(ind.genes)
    print(ind.gen)
    # print(sum(ind.errorTuple))
    print(meth.log(ind.error, 10))
    best10.append(ind.genes)
    if i >= 8:
        break

print(str(best10))

