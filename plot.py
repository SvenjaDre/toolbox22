import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(0, 10, 100)

plt.plot(x, 1/(x-1), "r--")
plt.savefig("build/plot.pdf")

