
import numpy as np
import matplotlib.pyplot as plt

# Definir a função f(x)
def f(x):
    return (x**2 - 1) / (x - 1)

# Criar valores de x próximos de 1
x_vals = np.linspace(0.5, 1.5, 400)
y_vals = f(x_vals)

# Plotar a função
plt.plot(x_vals, y_vals, label="f(x) = (x^2 - 1) / (x - 1)")
plt.axvline(x=1, color='r', linestyle='--', label='x = 1 (limite)')
plt.title('Limite de f(x) quando x tende a 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
