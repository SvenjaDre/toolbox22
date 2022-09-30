import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)

plt.plot(x, np.exp(x), color='purple', ls=':', label='Exp')
plt.legend()

plt.xlabel("x")
plt.ylabel("y")

plt.savefig("build/exp.pdf")
