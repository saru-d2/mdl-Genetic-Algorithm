# REPORT - Project on Genetic Algorithms  

### Team - dunder mifflin

Saravanan Senthil (2019101016), Abhijeeth Singam(2019101065)

## Introduction

The project revolved around using the genetic algorithm to find a vector of weights that performs well on a hidden dataset. This report will explain the logic behind it and explain some of the code.



How to run:

```python
python3 main.py
```



## Overview of Genetic Algorithm

```python
def newGeneration(oldgen):
    
    for i in oldgen.popList[:conf.BREEDING_POOL_SIZE]:
        total_error += i.error

    probs = []

   
    childGenesList = []

    while len(childGenesList) < conf.POPULATION_SIZE:
       
        indsToMate = np.random.choice(
            np.arange(0, conf.BREEDING_POOL_SIZE), 2, replace=False, p=probs)

        print("Selected mates: " + str(indsToMate))

        child1Genes, child2Genes = crossover(
            oldgen.popList[indsToMate[0]], oldgen.popList[indsToMate[1]])

				# on creation of individual object mutation takes place
        childGenesList.append(Individual(child1Genes))
        childGenesList.append(Individual(child2Genes))

        # childGenesList.append(child1Genes)

    bestofBothGenerations = oldgen.popList[:
                                           conf.NUM_PARENTS_PASSDOWN] + childGenesList
    bestofBothGenerations.sort(key=lambda x: x.error)

    utils.appendToSubmissionFile(toSubmit)

    return Population(bestofBothGenerations[0:conf.POPULATION_SIZE],
                      oldgen.genNumber + 1)

```

This function is called at the creation of each new generation, and predictably involves:

- selection
- crossover
- mutation

## Fitness function

The less error a vector received the fitter it was. We were given values to 2 kinds of errors train error and validation error, and initially the vector performed significantly better on the train set than the validation set



### Attempt 1
```python
	train + val
```

This worked well initially and enabled us to decrease the magnitudes of the train and validation errors, but after running this for an extended, we simply ended up with a vector that was overfit on train and validation together and performed terribly on the test set. 

### Attempt 2

```python
	(train - val)**2 * (train + val)**3
```

This was a failed attempt to reduce both the difference and the magnitude of the errors simultaneously. We attempted to reduce the difference so that it would perform similarly across the two sets and possible the test set as well. Achieving such consistency would mean that it would likely perform just as well on most other sets.

### Attempt 3

```python
	ERR_FACTOR*train + val
```

This was our successful attempt

## Selection Logic

- Sort population by fitness
- Take best conf.BREEDING_POOL_SIZE out of those
- Select 2 parents repeatedly based on their fitnesses
- Pass down the best conf.NUM_PARENTS_PASSDOWN parents



# Crossover Function

### attempt 1

- Take 2 parents and copy the vectors as child1 and child2
- Select 5 random indices
- switch the values of the children till that index

code :
``` python
def crossoverOld(par1, par2):
    # simply exchanging random genes
    child1Genes = par1.genes.copy()
    child2Genes = par2.genes.copy()
    randPrefix = random.randint(0, 11)
    indList = np.arange(0, randPrefix)
    # indList = np.random.choice(np.arange(0, 11), 5, replace=False)
    for index in indList:
        child1Genes[index], child2Genes[index] = child2Genes[
            index], child2Genes[index]

    return child1Genes, child2Genes
```

### attempt 2

- Take 2 parents

- Simulate binary crossover

code: 

```python
def crossover(par1, par2):
    # fancy, uses simulated binary crossover... keeps avg same, distributes all genes uniformly

    par1genes = par1.genes.copy()
    par2genes = par2.genes.copy()

    u = random.uniform(0, 1)

    nc = 3

    if u < 0.5:
        beta = (2 * u) ** (1 / (nc + 1))
    else:
        beta = (2 * (1 - u)) ** (-1 / (nc + 1))

    # nc decides how diff child will be from parent
    # beta is the similarity to the parents AKA spread factor

    child1genes = 0.5 * ((1 + beta) * par1genes + (1 - beta) * par2genes)
    child2genes = 0.5 * ((1 - beta) * par1genes + (1 + beta) * par2genes)

    # ensure that weigths are belong to [-10, 10]

    return child1genes, child2genes
```

Parameters to tune: nc (the divergence factor), it was initially set to 2 and later was set to 5 to produce similar children



## Mutation

```python
def mutate(genes):
    mutateProb = conf.MUTATE_PROB
    # numMutate = conf.NUM_MUTATE

    for index in range(11):
        # if it should be mutated or left alone
        if mutateProb >= random.random():
            if genes[index] == 0:
                genes[index] = random.uniform(-1e-20, 1e-20)
            # mutate!
            else:
                genes[index] *= random.uniform(-conf.MUTATE_FACTOR,
                                            conf.MUTATE_FACTOR) + 1
                # make sure weights are btw -10, 10
            genes[index] = min(genes[index], 10.0)
            genes[index] = max(genes[index], -10.0)

    return genes
```

Parameters to tune: 

- mutateProb: the probability that a gene of the vector get mutated

- mutateFactor: the factor by which it mutates



## Statistical information

Number of iterations to converge: we've restarted the algorithm several times, and each time its taken about 300 iterations to converge.



## various approches

- Starting from overfit: the most successful
- Starting with overfit with some features set to 0: in the middle
- Starting with random vectors: least successful



## additional tweaks (jugaad)

- Handpick vectors that perform well on the leaderboard from time to time





Img 1

Img 2

Img 3

