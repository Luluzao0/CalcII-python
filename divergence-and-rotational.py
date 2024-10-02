import numpy as np
import matplotlib.pyplot as plt

# Definir o campo vetorial F(x, y) = (P, Q)
X, Y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
P = -Y
Q = X

# Plotar o campo vetorial
plt.quiver(X, Y, P, Q)
plt.title('Campo Vetorial F(x, y) = (-y, x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
