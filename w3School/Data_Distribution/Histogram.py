
import numpy
import matplotlib.pyplot as plt

data = numpy.random.uniform(0, 5, 250)

plt.hist(data, 5)
plt.show()
