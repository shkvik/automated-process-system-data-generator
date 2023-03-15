import random as rnd
from multipledispatch import dispatch
from primitive.parameters import parameters


class parabola:

    def __init__(self, parameters: parameters) -> None:
        self.parameters = parameters
        

    @dispatch(int)
    def increase(self, time: int):
        step = self.parameters.maxHeight/time**2
        xCurrent: int = 0
        while(self.parameters.getLastValue() < self.parameters.maxHeight):
            xCurrent += 1
            self.parameters.sequense.append(xCurrent**2 * step +
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))
        return self
    

    @dispatch(int, int)
    def increase(self, time: int, maxHeight: float):
        if maxHeight > self.parameters.maxHeight:
            raise 'maxHeight cant be more than 100'

        step = maxHeight/time**2
        xCurrent = self.parameters.getLastValue()
        while(self.parameters.getLastValue() < maxHeight):
            xCurrent += 1
            self.parameters.sequense.append(xCurrent**2 * step +
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))
        return self