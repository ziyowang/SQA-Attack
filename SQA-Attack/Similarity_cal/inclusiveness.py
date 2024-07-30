import numpy as np
def calculate_inclusiveness_matrix(data_matrix, frequency_matrix):
    n = len(data_matrix)
    inclusiveness_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                # Calculate Nij, Ni, Nj for pair (i, j)
                Nij = data_matrix[i, j]
                Ni = np.count_nonzero(frequency_matrix[i])
                Nj = np.count_nonzero(frequency_matrix[j])

                if Ni == 0 or Nj == 0:
                    inclusiveness_matrix[i, j] = 1  # Avoid division by zero
                else:
                    inclusiveness_coefficient = Nij / np.sqrt(Ni * Nj)
                    inclusiveness_matrix[i, j] = 1 - inclusiveness_coefficient

    return inclusiveness_matrix