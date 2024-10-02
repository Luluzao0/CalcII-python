import numpy as np
import matplotlib.pyplot as plt

# Definir a função f(x)
def f(x):
    return np.sin(x)

# Valores de x e área sob a curva entre 0 e pi
x_vals = np.linspace(0, np.pi, 400)
y_vals = f(x_vals)

# Plotar a função e a área sob a curva
plt.plot(x_vals, y_vals, label='f(x) = sin(x)')
plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4)
plt.title('Área sob a curva de f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
