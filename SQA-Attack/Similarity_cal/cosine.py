import numpy as np
def calculate_cosine_matrix(data_matrix, frequency_matrix):
    n = len(data_matrix)
    cosine_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                # Calculate Nij, Ni, Nj for pair (i, j)
                Nij = data_matrix[i, j]
                Ni = np.count_nonzero(frequency_matrix[i])
                Nj = np.count_nonzero(frequency_matrix[j])

                if Ni == 0 or Nj == 0:
                    cosine_matrix[i, j] = 1  # Avoid division by zero
                else:
                    cosine_similarity = Nij / np.sqrt(Ni * Nj)
                    cosine_matrix[i, j] = 1 - cosine_similarity

    return cosine_matrix