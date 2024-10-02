
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])


# Determinante de uma matriz
determinante = np.linalg.det(A)
print(f"O determinante da matriz A é: {determinante}")

# Inversa de uma matriz
inversa = np.linalg.inv(A)
print(f"A inversa da matriz A é:\n{inversa}")

