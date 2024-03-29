import random as rnd
import math
from multipledispatch import dispatch
from primitive.parameters import parameters
import numpy as np

class sinusoid:

    def __init__(self, parameters: parameters) -> None:
        self.parameters = parameters
        self.tempSin: list[float] = []

    def getLastIndex(self) -> int:
        return len(self.tempSin) - 1
    
    def getLastValue(self) -> float:
        return self.tempSin[self.getLastIndex()]

    def increase(
            self,
            time: int,
            frequency: int = None,
            amplitude: float = None
              ):
        '''
        max = 100, min = 50
        '''
        
        if amplitude is None:
            amplitude = 0.5
        
        assert amplitude < 100 and amplitude > 0

        if frequency is None:
            frequency = 5

        x = np.arange(time)
        y = np.sin(2 * np.pi * frequency * x / time)
        y = y * amplitude

        if self.parameters.varianceMax != 0 or self.parameters.varianceMin != 0:
            y = [value + rnd.uniform(self.parameters.varianceMin,
                    self.parameters.varianceMax) for value in y]

        self.tempSin.extend(y)
        
        return self
    
    def align(self):
        final_y = [y + max(self.tempSin) for y in self.tempSin]
        self.parameters.sequense.extend(final_y)
        self.tempSin.clear()
