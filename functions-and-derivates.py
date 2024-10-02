import numpy as np
import matplotlib.pyplot as plt

# Definir a função e sua derivada
def f(x):
    return np.sin(x) * np.exp(x)

def df(x):
    return np.cos(x) * np.exp(x) + np.sin(x) * np.exp(x)

# Definir os pontos para plotar
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_vals = f(x_vals)
dy_vals = df(x_vals)

# Criar o gráfico
plt.plot(x_vals, y_vals, label='f(x) = sin(x) * exp(x)')
plt.plot(x_vals, dy_vals, label="f'(x) = derivada", linestyle='--')
plt.legend()
plt.title('Função e sua Derivada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
