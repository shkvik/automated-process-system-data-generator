import sys
sys.path.insert(0, 'lib')

import numpy as np

from processes.process import algorithm
from processes.utils import constrained_sum_sample_pos
import matplotlib.pyplot as plt
import random as rnd


class timePack:
    def __init__(self) -> None:

        self.pack = dict(
            static1= 1,
            grow=1,
            static2=1,
            fall=1,
            static3=1
        )

        pass
    
    def getSum(self) -> int:
        return sum(self.pack.values())


class сyclicSimpleWork:

    def __init__(self) -> None:

        self.algGrowFall    = algorithm()
        self.algBinEvent    = algorithm()
        self.algLinearEvent = algorithm()
        self.algIndependOne    = algorithm()
        self.algIndependTwo    = algorithm()

        self.time = timePack()
        self.dbgTime = 172


    def buildNormaSequence(self, tacts: int, switchMoment: int):
        flagBinEvent: bool = False
        for i in range(0, tacts):
            
            if i % switchMoment == 0 and i != 0:
                flagBinEvent = not flagBinEvent

            self.variance = rnd.uniform(0.0, 3.0)

            #all day seconds = 86400
            #sum = 860

            self.time.pack['static1']   = self.dbgTime
            self.time.pack['grow']      = self.dbgTime
            self.time.pack['static2']   = self.dbgTime
            self.time.pack['fall']      = self.dbgTime
            self.time.pack['static3']   = self.dbgTime

            self.dynGrowStaticfall(
                self.time.pack['static1'],
                self.time.pack['grow'],
                self.time.pack['static2'],
                self.time.pack['fall'],
                self.time.pack['static3']
            )
            self.dynLinearEvent(self.time.getSum(), flagBinEvent)
            self.dynBinEvent(self.time.getSum(), flagBinEvent)
            self.dynIndependOne(self.time.getSum())
            self.dynIndependTwo()

        return self
        
    def buildBreakSequence(self, tacts: int, switchMoment: int):
        flagBinEvent: bool = False
        for i in range(0, tacts):
            
            if i % switchMoment == 0 and i != 0:
                flagBinEvent = not flagBinEvent

            self.variance = rnd.uniform(0.0, 3.0)

            #all seconds in day = 86400
            #sum seconds in 1 cycle = 860
            time = constrained_sum_sample_pos(5, 860)

            self.time.pack['static1']   = time[0]
            self.time.pack['grow']      = time[1]
            self.time.pack['static2']   = time[2]
            self.time.pack['fall']      = time[3]
            self.time.pack['static3']   = time[4]

            self.dynGrowStaticfall(
                self.time.pack['static1'],
                self.time.pack['grow'],
                self.time.pack['static2'],
                self.time.pack['fall'],
                self.time.pack['static3']
            )
            self.dynLinearEvent(self.time.getSum(), flagBinEvent)
            self.dynBinEvent(self.time.getSum(), flagBinEvent)
            self.dynIndependOne(self.time.getSum())
            self.dynIndependTwo()

        return self        


    def dynIndependTwo(self):
        self.algIndependTwo.primitive.linear.increase(self.dbgTime, rnd.uniform(0, 100))
        self.algIndependTwo.primitive.linear.increase(self.dbgTime, rnd.uniform(0, 100))
        self.algIndependTwo.primitive.linear.increase(self.dbgTime, rnd.uniform(0, 100))
        self.algIndependTwo.primitive.linear.increase(self.dbgTime, rnd.uniform(0, 100))
        self.algIndependTwo.primitive.linear.increase(self.dbgTime, rnd.uniform(0, 100))

    def dynIndependOne(self, time: int):
        self.algIndependOne.primitive.linear.increase(time, rnd.uniform(0, 100))

    def dynLinearEvent(self, time: int, activate: bool = False) -> None:
        self.algLinearEvent.primitive.setVariance(-0.1,0.1)

        if activate:    
            incr = self.algLinearEvent.primitive.parameters.getLastValue() + 30
            incr = (incr, 100)[incr > 100]
            self.algLinearEvent.primitive.linear.increase(time, incr)
        else:
            incr = self.algLinearEvent.primitive.parameters.getLastValue() + 33
            incr = (0, incr)[incr > 100]
            self.algLinearEvent.primitive.linear.decrease(time, 100 - incr)

    def dynBinEvent(self, time: int, activate: bool = False) -> None:
        if activate:
            self.algBinEvent.primitive.static.true()
            self.algBinEvent.primitive.static.sequence(time)
        else:
            self.algBinEvent.primitive.static.false()
            self.algBinEvent.primitive.static.sequence(time)
        
    def dynGrowStaticfall(self,
            static1: int,
            grow: int,
            static2: int,
            fall: int,
            static3: int                  
        ) -> None:

        self.algGrowFall.primitive.setVariance(-self.variance,self.variance)
        self.algGrowFall.primitive.static.sequence(static1)
        self.algGrowFall.primitive.parabola.increase(grow)
        self.algGrowFall.primitive.static.sequence(static2)
        self.algGrowFall.primitive.parabola.decrease(fall)
        self.algGrowFall.primitive.static.sequence(static3)

    def getSequence(self):
        return (
            self.algGrowFall.primitive.getSequence(),
            self.algBinEvent.primitive.getSequence(),
            self.algLinearEvent.primitive.getSequence(),
            self.algIndependOne.primitive.getSequence(),
            self.algIndependTwo.primitive.getSequence()
        )



class eventProcessingWork():
    def __init__(self) -> None:
        self.algRndSinFluct = algorithm()
        pass
    
    def buildNormaSequence(self):
        self.dynRndSinFluct(1200, 6)
        self.dynRndSinFluct(500, 5)
        self.dynRndSinFluct(1200, 6)
        self.algRndSinFluct.primitive.sinusoid.align()
        return self

    def dynRndSinFluct(
            self,
            time: int = None,
            fluctuations: int = None
        ):
        
        watchDog: int = 0
        growDirect: bool = True

        allTime = 1000
        if fluctuations is None:
            fluctuations = 10

        period = time / fluctuations

        for index in range(1, fluctuations + 1):

            if index % ((fluctuations/2) + 2) == 0:
                growDirect = False

            if growDirect:
                watchDog += 1
            else:
                watchDog -= 1

            self.algRndSinFluct.primitive.sinusoid.increase(period, 1, watchDog)

        return self


    def getSequence(self):
        return (
            self.algRndSinFluct.primitive.getSequence()
        )


e = eventProcessingWork()

e.buildNormaSequence()

plt.plot(e.getSequence())
plt.show()
# b = сyclicSimpleWork()

# b = (b.buildNormaSequence(10, 7)
#         .buildBreakSequence(10, 7)
#         .buildNormaSequence(10, 7)
#         .buildBreakSequence(10, 7)
#         .buildNormaSequence(10, 7)
#         )

# alg, binEvent, linEvent, algIndependOne, algIndependTwo = b.getSequence()

# fig = plt.figure()

# colum = 6
# raw = 1

# ax_1 = fig.add_subplot(colum, raw, 1)
# ax_2 = fig.add_subplot(colum, raw, 2)
# ax_3 = fig.add_subplot(colum, raw, 3)
# ax_4 = fig.add_subplot(colum, raw, 4)
# ax_5 = fig.add_subplot(colum, raw, 5)
# ax_6 = fig.add_subplot(colum, raw, 6)

# ax_1.plot(alg)
# ax_2.plot(binEvent)
# ax_3.plot(linEvent)
# ax_4.plot(algIndependOne)
# ax_5.plot(algIndependTwo)

# ax_6.plot(alg)
# ax_6.plot(binEvent)
# ax_6.plot(linEvent)
# ax_6.plot(algIndependOne)
# ax_6.plot(algIndependTwo)

# print(min(linEvent))

# plt.show()