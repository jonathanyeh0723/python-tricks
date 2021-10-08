import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-10, 10, num=1000)
y = sigmoid(x)
plt.plot(x, y)
plt.show()
