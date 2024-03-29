import random as rnd
from multipledispatch import dispatch
from primitive.parameters import parameters


class static:

    def __init__(self, parameters: parameters) -> None:
        self.parameters = parameters

    def sequence(self, time: int):
        tempStaticValue = self.parameters.getLastValue()
        while(time != 0):
            time -= 1
            self.parameters.sequense.append(tempStaticValue + 
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))
        return self

    def true(self, time: int = None):
        self.parameters.sequense.append(self.parameters.maxHeight)

        if time is not None:
            self.sequence(time)
        return self

    def false(self, time: int = None):
        self.parameters.sequense.append(self.parameters.minHeight)

        if time is not None:
            self.sequence(time)
        return self
    
