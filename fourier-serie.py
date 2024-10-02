import numpy as np
import matplotlib.pyplot as plt

# Função periódica (onda quadrada) para decomposição em série de Fourier
def fourier_series(t, n_terms):
    f_approx = np.zeros_like(t)
    for n in range(1, n_terms + 1, 2):  # Apenas termos ímpares
        f_approx += (4 / (np.pi * n)) * np.sin(n * t)
    return f_approx

# Definir o intervalo de tempo
t = np.linspace(-np.pi, np.pi, 1000)

# Aproximar a função com diferentes números de termos
f_5_terms = fourier_series(t, 5)
f_10_terms = fourier_series(t, 10)
f_50_terms = fourier_series(t, 50)

# Plotar a série de Fourier aproximada com diferentes termos
plt.plot(t, f_5_terms, label='5 termos')
plt.plot(t, f_10_terms, label='10 termos')
plt.plot(t, f_50_terms, label='50 termos')
plt.title('Aproximação da Série de Fourier para uma Onda Quadrada')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.show()
