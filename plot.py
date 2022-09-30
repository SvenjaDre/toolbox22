import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), "b--")
plt.plot(x, 1/(x-1), "r--", label=r"$Juhu$")

plt.ylim(0,1)

plt.legend(loc="best")

plt.savefig("build/plot.pdf")




