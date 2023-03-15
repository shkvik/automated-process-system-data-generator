import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from multipledispatch import dispatch
from primitive.parameters import parameters
from primitive.parabola import parabola
from primitive.linear import linear


class generator:
    def __init__(self) -> None:

        self.varianceMax: float = 0.0
        self.varianceMin: float = 0.0

        self.maxHeight: float = 100
        self.minHeight: float = 0

        self.sequense:  list[float] = [1.0]

        self.parameters = parameters(
            self.varianceMax,
            self.varianceMin,
            self.maxHeight,
            self.minHeight,
            self.sequense
        )

        self.parabola = parabola(self.parameters)
        self.linear = linear(self.parameters)
    
    def setVariance(self, varianceMax: float = 0.0, varianceMin: float = 0.0):
        self.parameters.varianceMax = varianceMax
        self.parameters.varianceMin = varianceMin
        return self

    def getLastIndex(self) -> int:
        return len(self.sequense) - 1
    
    def getLastValue(self) -> float:
        return self.sequense[self.getLastIndex()]

    def equalizeSequense(self):
        if self.getLastValue() < self.varianceMin:
            self.sequense.append(0)

        if self.getLastValue() > self.varianceMax:
            self.sequense.append(100)

    def increaseLinear(self, time: int):
        step = self.maxHeight/time

        while(self.getLastValue() < self.maxHeight):
            self.sequense.append(self.getLastValue() + step +
                rnd.uniform(self.varianceMin, self.varianceMax))

        return self

    def decreaseLinear(self, time: int):
        step = self.maxHeight/time

        while(self.getLastValue() > self.minHeight):
            self.sequense.append(self.getLastValue() - step -
                rnd.uniform(self.varianceMin, self.varianceMax))

        return self
    
    def staticSequense(self, time: int):
        tempStaticValue = self.getLastValue()
        while(time != 0):
            time -= 1
            self.sequense.append(tempStaticValue + rnd.uniform(self.varianceMin, self.varianceMax))
        return self
    
    def logicFalse(self):
        self.sequense.append(self.minHeight)
        return self
    
    def logicTrue(self):
        self.sequense.append(self.maxHeight)
        return self

def DrawSignature(start: int, stop: int = None, letter: str = None, color: str = 'red'):
    plt.plot([start,start], [-10, 110], linestyle='dashed', c=color)
    plt.text(start + 10, 105, letter, fontsize=10)
    plt.plot([stop,stop], [-10, 110], linestyle='dashed', c=color)


gen1 = generator()

gen1.parabola.increase(100, 50)
gen1.parabola.increase(100, 60)
gen1.parabola.increase(100, 70)
gen1.parabola.decrease(100, 20)
gen1.parabola.decrease(100)
gen1.parabola.increase(100, 50)
gen1.linear.increaseLinear(100)
gen1.parabola.decrease(100, 20)
gen1.linear.decreaseLinear(100)

plt.plot(gen1.sequense)
plt.show()