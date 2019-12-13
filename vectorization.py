from pylab import *
import matplotlib.pyplot as plt

x = linspace(0, 10, 1000)
f = x**2*exp(-x)*sin(pi*x)

plt.plot(x, f)
plt.show()
