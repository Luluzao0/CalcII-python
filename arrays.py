import numpy as np
import matplotlib.pyplot as plt

# Definir dois vetores
v1 = np.array([2, 3, 1])
v2 = np.array([1, -1, 4])

# Soma de vetores
soma = v1 + v2
print(f"Soma de v1 e v2: {soma}")

# Produto escalar
produto_escalar = np.dot(v1, v2)
print(f"Produto escalar de v1 e v2: {produto_escalar}")

# Produto vetorial
produto_vetorial = np.cross(v1, v2)
print(f"Produto vetorial de v1 e v2: {produto_vetorial}")

# Visualizar os vetores no espaço 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar os vetores
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1', length=1)
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='v2', length=1)
ax.quiver(0, 0, 0, soma[0], soma[1], soma[2], color='g', label='Soma (v1 + v2)', length=1)

# Adicionar rótulos e legendas
ax.set_xlim([0, 3])
ax.set_ylim([-1, 4])
ax.set_zlim([0, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
