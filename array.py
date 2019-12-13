import matplotlib.pyplot as plt

m = [1.0, 2.0, 4.0, 6.0, 9.0, 11.0]
V = [0.13, 0.26, 0.50, 0.77, 1.15, 1.36]

plt.plot(m, V, linestyle= 'dashed', marker = 'o')
plt.xlabel('m (kg)')
plt.ylabel('V (l)')
plt.title('Arrays')

plt.show()
