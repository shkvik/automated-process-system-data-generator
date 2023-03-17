import sys
sys.path.insert(0, 'lib')

import numpy as np

from processes.process import algorithm
import matplotlib.pyplot as plt
import random as rnd

class builderAlgorithm:
    def __init__(self) -> None:
        pass
    
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


class builder:
    def __init__(self) -> None:

        self.algGrowFall    = algorithm()
        self.algBinEvent    = algorithm()
        self.algLinearEvent = algorithm()
        self.algIndependOne    = algorithm()
        self.algIndependTwo    = algorithm()

        self.algIndependOne.primitive.linear.increase(1, 50)
        self.algIndependTwo.primitive.linear.increase(1, 50)

        self.time = timePack()
        flagBinEvent: bool = False
        accumTime: int = 0
        self.dbgTime = 172

        for i in range(0, 50):
            
            if i % 4 == 0 and i != 0:
                flagBinEvent = not flagBinEvent

            self.variance   =  rnd.uniform(0.0, 3.0)

            # self.time.pack['static1']   = int(rnd.uniform(300, 500))
            # self.time.pack['grow']      = int(rnd.uniform(300, 500))
            # self.time.pack['static2']   = int(rnd.uniform(300, 500))
            # self.time.pack['fall']      = int(rnd.uniform(300, 500))
            # self.time.pack['static3']   = int(rnd.uniform(300, 500))

            #all day seconds = 86400
             #sum = 2000
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

            accumTime += self.time.getSum()

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
            incr = self.algLinearEvent.primitive.parameters.getLastValue() + 20
            incr = (0, incr)[incr > 100]
            self.algLinearEvent.primitive.linear.decrease(time, 100 - incr)

    def dynBinEvent(self, time: int, activate: bool = False) -> None:
        # self.algBinEvent.primitive.static.sequence(time)

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


b = builder()

alg, binEvent, linEvent, algIndependOne, algIndependTwo = b.getSequence()

fig = plt.figure()

colum = 6
raw = 1

ax_1 = fig.add_subplot(colum, raw, 1)
ax_2 = fig.add_subplot(colum, raw, 2)
ax_3 = fig.add_subplot(colum, raw, 3)
ax_4 = fig.add_subplot(colum, raw, 4)
ax_5 = fig.add_subplot(colum, raw, 5)
ax_6 = fig.add_subplot(colum, raw, 6)

ax_1.plot(alg)
ax_2.plot(binEvent)
ax_3.plot(linEvent)
ax_4.plot(algIndependOne)
ax_5.plot(algIndependTwo)

ax_6.plot(alg)
ax_6.plot(binEvent)
ax_6.plot(linEvent)
ax_6.plot(algIndependOne)
ax_6.plot(algIndependTwo)

plt.show()