import matplotlib.pyplot as plt
import numpy as np

# Definir o centro da circunferência e o raio
x_c, y_c = 0, 0
r = 5

# Criar os ângulos e calcular as coordenadas dos pontos da circunferência
theta = np.linspace(0, 2 * np.pi, 400)
x_vals = r * np.cos(theta) + x_c
y_vals = r * np.sin(theta) + y_c

# Plotar a circunferência
plt.plot(x_vals, y_vals, label="Circunferência")
plt.scatter(x_c, y_c, color='red', label="Centro")
plt.title("Equação da Circunferência")
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()
