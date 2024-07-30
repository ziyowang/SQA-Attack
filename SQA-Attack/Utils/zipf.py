import numpy as np
def inverse_zipf_distribution(n, beta):
    k = np.arange(1, n + 1)
    #weights=(n-k+1)**(-beta)
    #return weights/weights.sum()
    return 1.0 / (k ** beta) / np.sum(1.0 / (k ** beta))
def zipf_distribution(n, alpha):
    k = np.arange(1, n + 1)
    #weights=k ** (-alpha)
    #return weights/weights.sum()
    return 1.0 / (k ** alpha)