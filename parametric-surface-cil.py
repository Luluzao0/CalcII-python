import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir parâmetros cilíndricos
theta = np.linspace(0, 2 * np.pi, 50)
z = np.linspace(-2, 2, 50)
theta, z = np.meshgrid(theta, z)

# Definir o raio variável
r = 1 + z**2

# Converter para coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Criar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')

# Configurações do gráfico
ax.set_title('Superfície Paramétrica em Coordenadas Cilíndricas')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
