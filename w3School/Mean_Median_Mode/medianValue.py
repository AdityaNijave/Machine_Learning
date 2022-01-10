import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

medianSpeed = numpy.median(speed)
print(f"The median is : {medianSpeed}")

speed.sort()
print(f"The sorted list is : {speed}")
