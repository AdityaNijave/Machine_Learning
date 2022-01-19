import numpy
import matplotlib.pyplot as plt

bigData = numpy.random.uniform(0, 5, 100000)

plt.hist(bigData, 100)

plt.show()
