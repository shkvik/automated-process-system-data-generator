import sys
sys.path.insert(0, 'lib')

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

        self.time = timePack()
        flagBinEvent: bool = False
        accumTime: int = 0

        for i in range(0, 4):
            
            if i % 3 == 0 and i != 0:
                flagBinEvent = not flagBinEvent
                self.dynLinearEvent(accumTime, flagBinEvent)

            self.variance   =  rnd.uniform(0.0, 3.0)

            self.time.pack['static1']   = int(rnd.uniform(300, 500))
            self.time.pack['grow']      = int(rnd.uniform(300, 500))
            self.time.pack['static2']   = int(rnd.uniform(300, 500))
            self.time.pack['fall']      = int(rnd.uniform(300, 500))
            self.time.pack['static3']   = int(rnd.uniform(300, 500))

            self.dynGrowStaticfall(
                self.time.pack['static1'],
                self.time.pack['grow'],
                self.time.pack['static2'],
                self.time.pack['fall'],
                self.time.pack['static3']
            )

            self.dynLinearEvent(self.time.getSum())
            self.dynBinEvent(self.time.getSum(), flagBinEvent)
            accumTime += self.time.getSum()

    
    def dynLinearEvent(self, time: int, activate: bool = False) -> None:
        self.algLinearEvent.primitive.static.sequence(time)

        if activate:
            self.algLinearEvent.primitive.linear.increase(time)
        else:
            self.algLinearEvent.primitive.linear.decrease(time)

    def dynBinEvent(self, time: int, activate: bool = False) -> None:
        self.algBinEvent.primitive.static.sequence(time)

        if activate:
            self.algBinEvent.primitive.static.true() 
        else:
            self.algBinEvent.primitive.static.false()
        
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
            self.algLinearEvent.primitive.getSequence()
        )


b = builder()

alg, binEvent, linEvent = b.getSequence()

plt.plot(alg)
plt.plot(binEvent)
plt.plot(linEvent)
plt.show()