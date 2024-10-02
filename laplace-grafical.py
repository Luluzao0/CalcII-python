import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step
from scipy.signal import TransferFunction

# Definir a função de transferência H(s) = 1 / (s^2 + 2s + 2)
system = TransferFunction([1], [1, 2, 2])

# Calcular a resposta ao degrau
t, response = step(system)

# Plotar a resposta ao degrau
plt.plot(t, response)
plt.title('Resposta ao Degrau de H(s) = 1 / (s^2 + 2s + 2)')
plt.xlabel('Tempo t')
plt.ylabel('Resposta')
plt.grid(True)
plt.show()
