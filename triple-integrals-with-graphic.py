import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir a função f(x, y, z) = x * y * z
def f(x, y, z):
    return x * y * z

# Criar uma grade de pontos para o gráfico
x_vals = np.linspace(0, 1, 10)
y_vals = np.linspace(0, 1, 10)
z_vals = np.linspace(0, 1, 10)
X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)

# Calcular f(x, y, z)
F = f(X, Y, Z)

# Criar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=F.flatten(), cmap='viridis')

# Adicionar título e rótulos
ax.set_title('Função Tridimensional f(x, y, z) = x * y * z')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
