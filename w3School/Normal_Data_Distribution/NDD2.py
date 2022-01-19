import numpy
import matplotlib.pyplot as plt

ndd2 = numpy.random.normal(10, 2, 10000)
plt.hist(ndd2, 200)
plt.show()
