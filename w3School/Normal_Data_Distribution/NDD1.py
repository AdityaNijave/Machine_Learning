import numpy
import matplotlib.pyplot as plt

ndd1 = numpy.random.normal(5, 1, 10000)
plt.hist(ndd1, 100)
plt.show()
