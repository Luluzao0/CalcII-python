import numpy as np

# Definir uma matriz quadrada
A = np.array([[4, 1], [2, 3]])

# Calcular os autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

print(f"Autovalores da matriz A: {autovalores}")
print(f"Autovetores da matriz A:\n{autovetores}")

# Visualizar os autovetores
import matplotlib.pyplot as plt

# Criação do gráfico
fig, ax = plt.subplots()
ax.quiver(0, 0, autovetores[0, 0], autovetores[1, 0], angles='xy', scale_units='xy', scale=1, color='r', label='Autovetor 1')
ax.quiver(0, 0, autovetores[0, 1], autovetores[1, 1], angles='xy', scale_units='xy', scale=1, color='b', label='Autovetor 2')

# Configurações do gráfico
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.grid(True)
plt.title('Autovetores da Matriz A')
plt.show()
