from pylab import *
import matplotlib.pyplot as plt

h = 0.001
x = linspace(-5, 5, 1000)
df = zeros(1000, float)
for i in range(1000):
	df[i] = (exp(-(x[i] + h)**2)-exp(-(x[i] - h)**2))/(2*h)
plt.plot(x,df,'-.b')
plt.show()
