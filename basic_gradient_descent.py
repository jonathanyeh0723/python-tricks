import numpy as np

# define sigmoid
def sigmoid(x):
    return 1/(1+np.exp(-x))

# define derivative of sigmoid
def sigmoid_prime(x):
    return sigmoid(x) * (1-sigmoid(x))

# weight initialization
weight = np.array([-0.8, 0.5])
# input
x = np.array([0.1, 0.3])
# output
y = 0.2
# learning rate
learning_rate = 0.5

# linear combination
h = np.dot(x, weight)

# neural network output (y_hat)
y_hat = sigmoid(h)

# error (y - y_hat)
error = y - y_hat

# error term
error_term = error * sigmoid_prime(h)

# gradient descent step
del_w = learning_rate * error_term * x

print(del_w)

### Expect output
[-0.0039638  -0.01189141]
###
