import numpy
import sys

a = numpy.fromfile("datafile", dtype = numpy.int32)
a = a.reshape((int(sys.argv[1]),int(sys.argv[2])))

print a
