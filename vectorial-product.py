import numpy as np

# Definir dois vetores em 3D
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Calcular o produto vetorial
produto_vetorial = np.cross(v1, v2)
print(f"O produto vetorial de v1 e v2 é: {produto_vetorial}")
