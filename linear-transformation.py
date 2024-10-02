import scipy.linalg as la
import numpy as np

# Definir uma matriz
A = np.array([[4, 3], [6, 3]])

# Realizar a decomposição LU
P, L, U = la.lu(A)

print(f"Matriz L:\n{L}")
print(f"Matriz U:\n{U}")

# Definir a matriz A e o vetor b
A = np.array([[3, 2], [1, 2]])
b = np.array([1, 4])

# Resolver o sistema linear
x = np.linalg.solve(A, b)
print(f"A solução do sistema é: {x}")

# Definir uma matriz de transformação
T = np.array([[2, 0], [0, 1]])

# Definir um vetor
v = np.array([3, 2])

# Aplicar a transformação linear
v_transformado = np.dot(T, v)
print(f"O vetor transformado é: {v_transformado}")
