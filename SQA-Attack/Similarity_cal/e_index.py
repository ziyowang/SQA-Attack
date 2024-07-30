import numpy as np
def calculate_e_index_matrix(data_matrix, frequency_matrix):
   n = len(data_matrix)
   e_index_matrix = np.zeros((n, n))

   for i in range(n):
       for j in range(n):
           if i != j:
               # Calculate Nij, Ni, Nj for pair (i, j)
               Nij = data_matrix[i, j]
               Ni = np.count_nonzero(frequency_matrix[i])
               Nj = np.count_nonzero(frequency_matrix[j])

               if Ni == 0 or Nj == 0:
                   e_index_matrix[i, j] = 1  # Avoid division by zero
               else:
                   e_index_coefficient = Nij / np.sqrt(Ni * Nj)
                   e_index_matrix[i, j] = 1 - e_index_coefficient

   return e_index_matrix