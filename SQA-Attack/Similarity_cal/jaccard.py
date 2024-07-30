import numpy as np
def calculate_jaccard_matrix(data_matrix, frequency_matrix):
    n = len(data_matrix)
    jaccard_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                # Calculate Nij, Ni, Nj for pair (i, j)
                Nij = data_matrix[i, j]
                Ni = np.count_nonzero(frequency_matrix[i])
                Nj = np.count_nonzero(frequency_matrix[j])

                # Ensure data_matrix elements are integers for bitwise operation
                data_matrix[i] = data_matrix[i].astype(int)
                data_matrix[j] = data_matrix[j].astype(int)

                intersection_size = np.count_nonzero(np.bitwise_and(data_matrix[i], data_matrix[j]))
                union_size = Ni + Nj - intersection_size

                if union_size == 0:
                    jaccard_matrix[i, j] = 1  # Avoid division by zero
                else:
                    jaccard_coefficient = intersection_size / union_size
                    jaccard_matrix[i, j] = 1 - jaccard_coefficient

    return jaccard_matrix