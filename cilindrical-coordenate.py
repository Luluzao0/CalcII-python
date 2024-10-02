import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir as variáveis em coordenadas cilíndricas
theta = np.linspace(0, 2 * np.pi, 100)
z = np.linspace(0, 5, 100)
r = 2

# Converter para coordenadas cartesianas
theta, z = np.meshgrid(theta, z)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Criar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Adicionar título e rótulos
ax.set_title('Coordenadas Cilíndricas: Cilindro com r = 2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
