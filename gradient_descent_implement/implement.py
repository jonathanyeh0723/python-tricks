from data_prep import features, targets, features_test, targets_test
import numpy as np


def sigmoid(x):
    return 1 / (1+np.exp(-x))

n_records, n_features = features.shape
last_loss = 0

np.random.seed(42)

learn_rate = 0.5
epochs = 1000

weights = np.random.normal(loc=0, scale=n_features**-0.5, size=n_features)

for e in range(epochs):
    del_w = np.zeros(weights.shape)
    for x, y in zip(features.values, targets):
        output = sigmoid(np.dot(x, weights))
        error = y - output
        error_term = error * output * (1 - output)
        del_w += error_term * x

    weights += learn_rate * del_w / n_records

    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        out = sigmoid(np.dot(features, weights))
        loss = np.mean((out - targets) ** 2)
        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
tes_out = sigmoid(np.dot(features_test, weights))
predictions = tes_out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))
