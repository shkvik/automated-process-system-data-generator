import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

class Generator:
    def __init__(self) -> None:

        self.maxHeight: float = 100
        self.minHeight: float = 0
        
        self.sequense:  list[float] = [1.0]
    
    def SetVariance(self, varianceMax: float = 0.0, varianceMin: float = 0.0):
        self.varianceMax: float = varianceMax
        self.varianceMin: float = varianceMin

    def GetLastIndex(self) -> int:
        return len(self.sequense) - 1
    
    def GetLastValue(self) -> float:
        return self.sequense[self.GetLastIndex()]

    def EqualizeSequense(self):
        if self.GetLastValue() < self.varianceMin:
            self.sequense.append(0)

        if self.GetLastValue() > self.varianceMax:
            self.sequense.append(100)

    def IncreaseLinear(self, time: int):
        step = self.maxHeight/time

        while(self.GetLastValue() < self.maxHeight):
            self.sequense.append(self.GetLastValue() + step +
                rnd.uniform(self.varianceMin, self.varianceMax))

        return self

    def DecreaseParabol(self, time: int):
        step = self.maxHeight/time**2
        xCurrent: int = 0
        while(self.GetLastValue() > self.minHeight):
            xCurrent += 1
            self.sequense.append(xCurrent**2 * -step + self.maxHeight +
                rnd.uniform(self.varianceMin, self.varianceMax))
        return self

    def IncreaseParabol(self, time: int):
        step = self.maxHeight/time**2
        xCurrent: int = 0
        while(self.GetLastValue() < self.maxHeight):
            xCurrent += 1
            self.sequense.append(xCurrent**2 * step +
                rnd.uniform(self.varianceMin, self.varianceMax))
        return self

    def DecreaseLinear(self, time: int):
        step = self.maxHeight/time

        while(self.GetLastValue() > self.minHeight):
            self.sequense.append(self.GetLastValue() - step -
                rnd.uniform(self.varianceMin, self.varianceMax))

        return self
    
    def StaticSequense(self, time: int):
        tempStaticValue = self.GetLastValue()
        while(time != 0):
            time -= 1
            self.sequense.append(tempStaticValue + rnd.uniform(self.varianceMin, self.varianceMax))
        return self
    
    def LogicFalse(self):
        self.sequense.append(self.minHeight)
        return self
    
    def LogicTrue(self):
        self.sequense.append(self.maxHeight)
        return self

a = Generator()
a.SetVariance(-1.5, 1.5)
a.IncreaseLinear(100)

a.SetVariance(-1.5, 1.5)
a.StaticSequense(100)

a.DecreaseLinear(100)

a.SetVariance(-0.5, 0.5)
a.StaticSequense(100)
a.SetVariance(-1.5, 1.5)

a.IncreaseParabol(100)
a.DecreaseParabol(100)


plt.plot(a.sequense)

def DrawSignature(start: int, stop: int, letter: str):
    plt.plot([start,start], [-10, 110], linestyle='dashed', c='red')
    plt.text(start + 10, 105, letter, fontsize=10)
    plt.plot([stop,stop], [-10, 110], linestyle='dashed', c='red')

DrawSignature(300, 600, 'Hey you')

# sns.pairplot(df)

plt.show()