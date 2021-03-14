import config as conf
import os
import json


def prevDataExists():
    return os.path.exists(conf.PREV_RESULTS_FILE)


def loadPrevData():
    with open(conf.PREV_RESULTS_FILE) as fd:
        return json.load(fd)


def print_stats(population, gen):
    print('gen ' + str(gen))
    print('avg ' + str(population.getMeanError()))
    print('best ' + str(population.getFittest().error))


def writeJSON(genData):

    temp = {'PrevGens': []}
    genDict = {'genNumber': genData.genNumber, 'popList': []}
    for each in genData.popList:
        genDict['popList'].append({
            'genes': each.genes.tolist(),
            'errorTuple': each.errorTuple
        })

    temp['PrevGens'].append(genDict)
    with open(conf.PREV_RESULTS_FILE, 'w') as fd:
        json.dump(temp, fd, indent=4)


def appendGenToFile(genData):
    # reading for purposes of appending
    if conf.TEST:

        return
    temp = loadPrevData()
    genDict = {'genNumber': genData.genNumber, 'popList': []}
    for each in genData.popList:
        genDict['popList'].append({
            'genes': each.genes.tolist(),
            'errorTuple': each.errorTuple
        })

    temp['PrevGens'].append(genDict)
    with open(conf.PREV_RESULTS_FILE, 'w') as fd:
        json.dump(temp, fd, indent=4)


def submissionFileExists():
    return os.path.exists(conf.SUBFILE)


def appendToSubmissionFile(obj):
    # print(obj)
    if submissionFileExists():
        print(submissionFileExists())
        with open(conf.SUBFILE) as fd:
            prevData = json.load(fd)
    else:
        prevData = {'PrevGens': []}
        with open(conf.SUBFILE, 'w') as fd:
            json.dump(prevData, fd, indent=4)

    curTup = {'initial': [], 'selected': [], 'beforeMut': [], 'afterMut': []}

    for i in obj['init']:
        curTup['initial'].append(i.tolist())

    for i in obj['selected']:
        curTup['selected'].append(i.tolist())

    for i in obj['beforeMut']:
        curTup['beforeMut'].append(i.tolist())

    for i in obj['afterMut']:
        curTup['afterMut'].append(i.tolist())

    prevData['PrevGens'].append(curTup)
    with open(conf.SUBFILE, 'w') as fd:
        json.dump(prevData, fd, indent=4)
