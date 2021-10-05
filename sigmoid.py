import numpy as np


def softmax(L):
    return np.exp(L) / sum(np.exp(L))


if __name__ == "__main__":
    data = [5, 6, 7]
    print(np.exp(data))
    print(sum(np.exp(data)))
    print(softmax(data))
