import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6) # array([0, 1, 2, 3, 4, 5])
y = np.exp(x)
plt.plot(x, y)
plt.ylim(0, 160)
plt.show()
