import random as rnd
import math
import pandas as pd 
import numpy as np


# from primitive.parameters import parameters
from parameters import parameters
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns


def get_all_divisors_brute(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

class event:

    def __init__(self) -> None:
        self.parametersPrcss = parameters(
            varianceMax = 0.0,
            varianceMin = 0.0,
            maxHeight   = 100.0,
            minHeight   = 0.0,
            sequense    = []
        )

        self.parametersEvent = parameters(
            varianceMax = 0.0,
            varianceMin = 0.0,
            maxHeight   = 100.0,
            minHeight   = 0.0,
            sequense    = []
        )

    def increaseEventSin(self,
        time: int,
        maxHeight: float = None
    ):
        if maxHeight is None:
            maxHeight = 1

        step = time/180

        for index in range(0, time + 1):
            self.parametersEvent.sequense.append(math.sin(math.radians(index/step)) * maxHeight)

        return self
    
    
    def sequenceEventSin(self, time: int):
        for i in range(0, time):
            self.parametersEvent.sequense.append(0)

        return self

    def decreasePrc(self, time: int, maxHeight: float = None):

        limit: float = self.parametersPrcss.getLastValue()

        if maxHeight is not None:
            assert(maxHeight < self.parametersPrcss.maxHeight 
                or maxHeight > self.parametersPrcss.minHeight)
            
            show = self.parametersPrcss.maxHeight - maxHeight
            limit = abs(limit - (self.parametersPrcss.maxHeight - maxHeight))
        
        step = limit/time 

        for index in range(0, time + 1):

            newValue = (self.parametersPrcss.getLastValue() - step -
                            rnd.uniform(-1.5, 1.5))

            if newValue <= self.parametersPrcss.minHeight:
                self.parametersPrcss.sequense.append(self.parametersPrcss.minHeight)
            elif newValue > 100:
                self.parametersPrcss.sequense.append(self.parametersEvent.maxHeight)
            else:
                self.parametersPrcss.sequense.append(newValue)

        self.sequenceEventSin(time + 1)


    def rndProcess(self, time: int, maxHeight: float = None):
        
        limit: float = self.parametersPrcss.maxHeight - self.parametersPrcss.getLastValue()

        if maxHeight is not None:
            assert(maxHeight < self.parametersPrcss.maxHeight 
                or maxHeight > self.parametersPrcss.minHeight)
            limit = limit - (self.parametersPrcss.maxHeight - maxHeight)

        step = limit/time
        
        block = True
        swithOff = False

        for index in range(0, time + 1):

            newValue = (self.parametersPrcss.getLastValue() + step +
                    rnd.uniform(-1.5, 1.5))

            if newValue > 100:
                self.parametersPrcss.sequense.append(self.parametersEvent.maxHeight)
            elif newValue < 0:
                self.parametersPrcss.sequense.append(self.parametersEvent.minHeight)
            else:
                self.parametersPrcss.sequense.append(newValue)
                
            if self.parametersPrcss.getLastValue() > 50 and not swithOff:
                swithOff = True
                block = False

            if not block:
                self.sequenceEventSin(index)
                self.increaseEventSin(int((time + 1) * 0.2), 100)
                self.sequenceEventSin((time + 1) - (index + int((time) * 0.2)))
                block = True

        if not swithOff:
            self.sequenceEventSin(time - 1)

    def buildRndSeqs(self):
        allSecondsInDay = 86400

        res = list(get_all_divisors_brute(allSecondsInDay))
        deleters: list[int] = []
        for i in range(0, len(res) - 1):
            if res[i] >= 100 and res[i] % 2 == 0:
                if (allSecondsInDay / res[i]) % 2 == 0:
                    deleters.append(res[i])

        self.time    = int(deleters[rnd.randint(0, len(deleters) - 1)])
        self.tacts   = int((allSecondsInDay / self.time)/2)

        for i in range(0, self.tacts):
            self.rndProcess(self.time, rnd.uniform(self.parametersPrcss.getLastValue(), 100))
            self.decreasePrc(self.time, rnd.uniform(self.parametersPrcss.getLastValue(), 100))

    def getSequenceEvent(self):
        return self.parametersEvent.sequense
    
    def getSequencePrcss(self):
        return self.parametersPrcss.sequense


def compression(listNode: list[float]):
    listNode = listNode[0:80000:100]
    return listNode



def prepareDataPd():
    colum = 10

    sequences = []
    for i in range(0, colum):
        tmp = event()
        tmp.buildRndSeqs()
        sequences.append(compression(tmp.getSequenceEvent()))
        sequences.append(compression(tmp.getSequencePrcss()))

    res = alignDicts(sequences)

    return pd.DataFrame(res)


def prepareDataNpArray():
    colum = 10

    sequences = []
    for i in range(0, colum):
        tmp = event()
        tmp.buildRndSeqs()
        sequences.append(compression(tmp.getSequenceEvent()))
        sequences.append(compression(tmp.getSequencePrcss()))

    res = alignToNpArray(sequences)

    return res



def alignDicts(nodeList: list[list[float]] = []):
    tmp: list[int] = []
    result = {}

    for i in range(0, len(nodeList)):
        tmp.append(len(nodeList[i]))

    tmp.sort()

    for i in range(0, len(nodeList)):
        nodeList[i] = nodeList[i][:tmp[0]]
        result['node' + str(i)] = nodeList[i]
        print('node[' + str(i) + ']: ' + str(len(nodeList[i])))

    return result


def alignToNpArray(nodeList: list[list[float]] = []):
    tmp: list[int] = []
    result = []

    for i in range(0, len(nodeList)):
        tmp.append(len(nodeList[i]))

    tmp.sort()

    for i in range(0, len(nodeList)):
        nodeList[i] = nodeList[i][:tmp[0]]
        result.append(np.array(nodeList[i]))
        print('np array [' + str(i) + ']: ' + str(len(nodeList[i])))

    return result


# colum = 10

# sequences = []
# for i in range(0, colum):
#     tmp = event()
#     tmp.buildRndSeqs()
#     sequences.append(compression(tmp.getSequenceEvent()))
#     sequences.append(compression(tmp.getSequencePrcss()))


# fig = plt.figure()


# raw = 1

# axs = []
# for i in range(0, colum):
#     axs.append(fig.add_subplot(colum, raw, i + 1))
#     axs[i].plot(compression(sequences[i]))




# res = alignLists(sequences)

# df = pd.DataFrame(res)

# df.to_csv('GFG.csv') 


#plt.show()