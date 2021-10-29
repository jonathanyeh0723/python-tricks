import numpy as np
from data_prep import features, targets, features_test, targets_test

np.random.seed(21)

def sigmoid(x):
    return 1/(1+np.exp(-x))

np.random.seed(21)

n_hidden = 2
epochs = 900
learnrate = 0.005

n_records, n_features = features.shape
last_loss = None

weights_input_hidden = np.random.normal(scale=n_features**-0.5, size=(n_features, n_hidden))
weights_hidden_output = np.random.normal(scale=n_features**-0.5, size=n_hidden)

for e in range(epochs):
    del_w_input_hidden = np.zeros(weights_input_hidden.shape)
    del_w_hidden_output = np.zeros(weights_hidden_output.shape)
    for x, y in zip(features.values, targets):
        
        hidden_input = np.dot(x, weights_input_hidden)
        hidden_output = sigmoid(hidden_input)
        
        output_in = np.dot(hidden_output, weights_hidden_output)
        output = sigmoid(output_in)
        
        error = y - output
        error_term = error * output * (1 - output)
        
        hidden_error = np.dot(error_term, weights_hidden_output)
        hidden_error_term = hidden_error * hidden_output * (1 - hidden_output)
        
        del_w_hidden_output += error_term * hidden_output
        del_w_input_hidden += hidden_error_term * x[:, None]
    
    weights_input_hidden += learnrate * del_w_input_hidden / n_records
    weights_hidden_output += learnrate * del_w_hidden_output / n_records
    
    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        hidden_output = sigmoid(np.dot(x, weights_input_hidden))
        out = sigmoid(np.dot(hidden_output,
                             weights_hidden_output))
        loss = np.mean((out - targets) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
hidden = sigmoid(np.dot(features_test, weights_input_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_output))
predictions = out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))
