import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from multipledispatch import dispatch
from primitive.parameters import parameters
from primitive.parabola import parabola
from primitive.linear import linear
from primitive.static import static
from primitive.sinusoid import sinusoid

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
        self.static = static(self.parameters)
        self.sinusoid = sinusoid(self.parameters)


def DrawSignature(start: int, stop: int = None, letter: str = None, color: str = 'red'):
    plt.plot([start,start], [-10, 110], linestyle='dashed', c=color)
    plt.text(start + 10, 105, letter, fontsize=10)
    plt.plot([stop,stop], [-10, 110], linestyle='dashed', c=color)


gen1 = generator()


gen1.sinusoid.increase(500, 1, 2 * 10)
gen1.sinusoid.increase(500, 1, 1 * 10)
gen1.sinusoid.increase(500, 1, 2 * 10)
gen1.sinusoid.increase(500, 1, 3 * 10)
gen1.sinusoid.increase(500, 1, 4 * 10)
gen1.sinusoid.increase(500, 1, 3 * 10)
gen1.sinusoid.increase(500, 1, 2 * 10)
gen1.sinusoid.align()

plt.plot(gen1.sequense)
plt.show()