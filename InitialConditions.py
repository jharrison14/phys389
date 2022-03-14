import numpy as np

def line(x):
    return 2*x + 4

def two_top_hat(x):
    if x <= 2:
        return 1
    else:
        return 0

def gaussian(x):
    return np.exp(-2*(x-2)**2)
