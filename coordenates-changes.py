import numpy as np
import matplotlib.pyplot as plt

# Definir a função em coordenadas polares
theta = np.linspace(0, 2 * np.pi, 400)
r = 1 + np.cos(theta)

# Converter para coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plotar a curva em coordenadas polares
plt.plot(x, y)
plt.title('Curva em Coordenadas Polares: r = 1 + cos(theta)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
