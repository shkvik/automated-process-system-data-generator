import random as rnd
from multipledispatch import dispatch
from primitive.parameters import parameters

class linear:

    def __init__(self, parameters: parameters) -> None:
        self.parameters = parameters

    def increase(self, time: int):
        step = (self.parameters.maxHeight - self.parameters.getLastValue()) /time 

        for index in range(0, time):
            self.parameters.sequense.append(self.parameters.getLastValue() + step +
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))

        return self
    
    def decrease(self, time: int):
        step = (self.parameters.getLastValue()) /time 

        for index in range(0, time):
            self.parameters.sequense.append(self.parameters.getLastValue() - step -
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))

        return self