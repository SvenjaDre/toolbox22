import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(0, 10, 100)

plt.plot(x, x**2, "r--")
plt.savefig("build/plot.pdf")

