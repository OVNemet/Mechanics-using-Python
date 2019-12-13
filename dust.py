import random
from pylab import *
import matplotlib.pyplot as plt

n = 10000
x = zeros(n+1, int)
for i in range(n):
	if randint(1, 6) <= 3:
		dx = -1
	else:
		dx = 1
	x[i] = x[i-1] + dx
	if x[i] > 5:
		x[i] = 5
	if x[i] < -5:
		x[i] = -5

plt.plot(x)
plt.xlabel('i')
plt.ylabel('x(i)')
plt.show()
