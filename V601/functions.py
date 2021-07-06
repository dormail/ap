# functions.py

import numpy as np

# get n-th largest element
# one-indexed
def nth_largest(x, n=1):
    x = np.sort(x)
    return x[-n]


# L_inf normalize
def normalize(x):
    return x / nth_largest(x, n=1)

# differentiate y with respect to x
def differentiate(x, y):
    n = np.shape(y)[0]
    x_dif = np.array([])
    y_dif = np.array([])

    for i in range(0, n-1):
        y_dif = np.append(y_dif, (y[i+1] - y[i]) / (x[i+1] - x[i]))
        x_dif = np.append(x_dif, (x[i] + x[i+1])/2)
        
    return x_dif, y_dif

