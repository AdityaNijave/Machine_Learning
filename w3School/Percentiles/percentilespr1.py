import numpy

ages = [31,5,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentiles = numpy.percentile(ages,90)

print(percentiles)
