from pylab import *
import matplotlib.pyplot as plt
import random

x = cumsum(2*(randint(1,6,1000)<=3)-1)
plt.plot(x)
plt.show()
