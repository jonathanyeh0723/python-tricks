import numpy as np

print("----- np.dot -----")
print('''numpy.dot(a, b, out=None): Dot product of two arrays. Specifically,
If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.''')
print("-----  -----")

def sigmoid(x):
    return 1/(1+np.exp(-x))

# network size
n_input = 4
n_hidden = 3
n_output = 2

print(f'network structure: {n_input} x {n_hidden} x {n_output}')

# make some data
np.random.seed(42)
X = np.random.randn(4)

# initial weights
weights_i_h = np.random.normal(loc=0, scale=0.1, size=(n_input, n_hidden))
weights_h_o = np.random.normal(loc=0, scale=0.1, size=(n_hidden, n_output))

# check the shape
print(f'features shape: {X.shape}')
print(f'inputs to hidden layers shape: {weights_i_h.shape}')

hidden_layer_input = np.dot(X, weights_i_h)
print(f'hidden layer input: {hidden_layer_input}')

hidden_layer_output = sigmoid(hidden_layer_input)
print(f'hidden layer output: {hidden_layer_output}')

final_layer_input = np.dot(hidden_layer_output, weights_h_o)
print(f'final layer input: {final_layer_input}')

final_layer_output = sigmoid(final_layer_input)
print(f'final layer output: {final_layer_output}')
