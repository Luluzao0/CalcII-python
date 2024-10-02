import matplotlib.pyplot as plt
import numpy as np

# Definir os pontos P e Q
x1, y1 = 1, 2
x2, y2 = 4, 6

# Calcular o coeficiente angular (m)
m = (y2 - y1) / (x2 - x1)

# Definir a função da reta
def reta(x):
    return m * (x - x1) + y1

# Criar o gráfico
x_vals = np.linspace(0, 5, 100)
y_vals = reta(x_vals)

plt.plot(x_vals, y_vals, label="Reta")
plt.scatter([x1, x2], [y1, y2], color='red', label="Pontos P e Q")
plt.title("Equação da Reta")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
