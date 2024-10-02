import numpy as np
import matplotlib.pyplot as plt

# Definir a função e sua derivada
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Gerar valores de x
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_vals = f(x_vals)
dy_vals = df(x_vals)

# Plotar a função e sua derivada
plt.plot(x_vals, y_vals, label='f(x) = sin(x)')
plt.plot(x_vals, dy_vals, label="f'(x) = cos(x)", linestyle='--')
plt.title('Função e sua Derivada')
plt.xlabel('x')
plt.ylabel('f(x), f\'(x)')
plt.legend()
plt.grid(True)
plt.show()
