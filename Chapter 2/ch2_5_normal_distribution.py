import numpy as np
import matplotlib.pyplot as plt

results_1 = []
results_2 = []

def normal(x, mu, sigma):
	P = (1 / (np.sqrt(2*np.pi*sigma**2)) * np.e**(-(x-mu)**2 / (2*sigma**2) ) )
	return P

x = np.linspace(-5, 5, 1000)
results_1 = normal(x, 0, 1)
results_2 = normal(x, 0, 0.5)

plt.plot(x, results_1)
plt.plot(x, results_2)
plt.show()
