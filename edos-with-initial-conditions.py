import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definir a equação diferencial dy/dt = -2y
def model(y, t):
    dydt = -2 * y
    return dydt

# Condição inicial
y0 = 5

# Valores de tempo
t = np.linspace(0, 5, 100)

# Resolver a EDO
y = odeint(model, y0, t)

# Plotar a solução
plt.plot(t, y)
plt.title('Solução de dy/dt = -2y com y(0) = 5')
plt.xlabel('Tempo t')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()
