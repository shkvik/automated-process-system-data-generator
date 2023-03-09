from lib.primitive_operations import generator
import matplotlib.pyplot as plt

gen = generator()

gen.setVariance(-1.0,1.0)
gen.increaseLinear(100)

plt.plot(gen.sequense)
plt.show()