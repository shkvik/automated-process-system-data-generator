import random as rnd
from multipledispatch import dispatch
from primitive.parameters import parameters


class parabola:

    def __init__(self, parameters: parameters) -> None:
        self.parameters = parameters
        
    def increase(self, time: int, maxHeight: float = None):
        if maxHeight is None:
            maxHeight = self.parameters.maxHeight 

        if maxHeight > self.parameters.maxHeight:
            raise Exception('minHeight cant be more than {max}'
                .format(max=self.parameters.maxHeight))

        bias = self.parameters.getLastValue()
        step = (maxHeight - bias)/time**2

        for index in range(0, time):
            self.parameters.sequense.append(index**2 * step + bias +
                rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))

        return self
    

    def decrease(self, time: int, minHeight: float = None):
        maxHeight = self.parameters.maxHeight

        if minHeight is None:
            minHeight = self.parameters.minHeight
            maxHeight = self.parameters.getLastValue()
        else:
            pass
            
        if minHeight < self.parameters.minHeight:
            raise Exception('minHeight cant be less than {min}'
                .format(min=self.parameters.minHeight))
        
        bias = self.parameters.getLastValue()
        step = bias/time**2
        

        for index in range(0, time):
            if self.parameters.getLastValue() > minHeight:

                act1 = index**2 * -step
                watch = act1 + bias

                result: float
                if watch < minHeight:
                    result = (self.parameters.getLastValue() + 
                        rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))
                else:
                    result = (watch + 
                        rnd.uniform(self.parameters.varianceMin, self.parameters.varianceMax))

                self.parameters.sequense.append(result)
            else:
                break

        return self