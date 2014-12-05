#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

start = int(sys.argv[2])
end = -1
firstColoumn = int(sys.argv[4]) - 1
secondColoumn = int(sys.argv[5]) - 1

print start
print end

with open(sys.argv[1]) as f:
     data = f.read()

data = data.split('\n')
print data
x = [row.split(' ')[firstColoumn] for row in data[start:end]]
y = [row.split(' ')[secondColoumn] for row in data[start:end]]
print x
print y

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Plot title...")
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')
ax1.plot(x,y, c='r', label='the data')
leg = ax1.legend()

plt.show()
