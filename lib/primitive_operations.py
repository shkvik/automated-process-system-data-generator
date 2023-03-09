import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

class generator:
    def __init__(self) -> None:

        self.varianceMax: float = 0.0
        self.varianceMin: float = 0.0

        self.maxHeight: float = 100
        self.minHeight: float = 0
        
        self.sequense:  list[float] = [1.0]
    
    def setVariance(self, varianceMax: float = 0.0, varianceMin: float = 0.0):
        self.varianceMax = varianceMax
        self.varianceMin = varianceMin

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

    def decreaseParabol(self, time: int):
        step = self.maxHeight/time**2
        xCurrent: int = 0
        while(self.getLastValue() > self.minHeight):
            xCurrent += 1
            self.sequense.append(xCurrent**2 * -step + self.maxHeight +
                rnd.uniform(self.varianceMin, self.varianceMax))
        return self

    def increaseParabol(self, time: int):
        step = self.maxHeight/time**2
        xCurrent: int = 0
        while(self.getLastValue() < self.maxHeight):
            xCurrent += 1
            self.sequense.append(xCurrent**2 * step +
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

def DrawSignature(start: int, stop: int, letter: str):
    plt.plot([start,start], [-10, 110], linestyle='dashed', c='red')
    plt.text(start + 10, 105, letter, fontsize=10)
    plt.plot([stop,stop], [-10, 110], linestyle='dashed', c='red')
