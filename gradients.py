import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir a função f(x, y)
def f(x, y):
    return np.sin(x) * np.cos(y)

# Criar uma grade de valores de x e y
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_vals = np.linspace(-2 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f(X, Y)

# Criar o gráfico 3D da função
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Adicionar título e rótulos
ax.set_title('Superfície de f(x, y) = sin(x) * cos(y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.show()
