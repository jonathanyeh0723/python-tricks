import numpy as np


def softmax(L):
    return np.exp(L) / sum(np.exp(L))


if __name__ == "__main__":
    data = [5, 6, 7]
    print(np.exp(data))
    print(sum(np.exp(data)))
    print(softmax(data))
    
### Expect output
[ 148.4131591   403.42879349 1096.63315843]
1648.4751110237703
[0.09003057 0.24472847 0.66524096]
###
