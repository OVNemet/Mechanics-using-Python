import matplotlib.pyplot as plt

run100m = open("100m.d")

t = run100m[:,0]
x = run100m[:,1]

plt.plot(t,x)
plt.show()
