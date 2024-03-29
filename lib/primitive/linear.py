import random as rnd
import math
from multipledispatch import dispatch
from primitive.parameters import parameters
from processes.utils import drange

class linear:

    def __init__(self, parameters: parameters) -> None:
        self.parameters = parameters

    def increase(self, time: int, maxHeight: float = None):
        
        limit: float = self.parameters.maxHeight - self.parameters.getLastValue()

        if maxHeight is not None:
            assert(maxHeight < self.parameters.maxHeight 
                or maxHeight > self.parameters.minHeight)
            limit = limit - (self.parameters.maxHeight - maxHeight)

        step = limit/time

        for index in range(0, time):
            self.parameters.sequense.append(self.parameters.getLastValue() + step +
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))

        return self


    def increaseEventSin(self,
        time: int,
        maxHeight: float = None,
        floatingLength: int = None
    ):
        if maxHeight is None:
            maxHeight = 1

        step = time/180

        for index in range(0, time + 1):
            self.parameters.sequense.append(math.sin(math.radians(index/step)) * maxHeight)

        return self


    def decrease(self, time: int, maxHeight: float = None):

        limit: float = self.parameters.getLastValue()

        if maxHeight is not None:
            assert(maxHeight < self.parameters.maxHeight 
                or maxHeight > self.parameters.minHeight)
            
            show = self.parameters.maxHeight - maxHeight
            limit = abs(limit - (self.parameters.maxHeight - maxHeight))
        
        step = limit/time 

        for index in range(0, time):
            if self.parameters.getLastValue() < self.parameters.minHeight:
                self.parameters.sequense.append(self.parameters.minHeight)
            else:
                self.parameters.sequense.append(self.parameters.getLastValue() - step -
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))

        return self