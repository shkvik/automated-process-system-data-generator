import random as rnd
from multipledispatch import dispatch

from primitive.parameters import parameters
from primitive.parabola import parabola
from primitive.linear import linear

class primitive:
    def __init__(self) -> None:

        self.parameters = parameters(
            varianceMax=0.0,
            varianceMin=0.0,
            maxHeight=100.0,
            minHeight=0.0,
            sequense= [1.0] 
        )

        self.parabola = parabola(self.parameters)
        self.linear = linear(self.parameters)

    def setVariance(self, varianceMax: float = 0.0, varianceMin: float = 0.0):
        self.parameters.varianceMax = varianceMax
        self.parameters.varianceMin = varianceMin
        return self