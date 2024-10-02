import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Definir a função de onda quadrada
t = np.linspace(0, 1, 500, endpoint=False)
square_wave = np.sign(np.sin(2 * np.pi * 5 * t))

# Aplicar a transformada de Fourier
fft_wave = fft(square_wave)
frequencies = fftfreq(t.size, d=t[1] - t[0])

# Plotar a onda e seu espectro de Fourier
plt.subplot(2, 1, 1)
plt.plot(t, square_wave)
plt.title('Onda Quadrada no Domínio do Tempo')
plt.xlabel('t')
plt.grid(True)
plt.subplot(2, 1, 2)
plt.stem(frequencies, np.abs(fft_wave))
plt.title('Transformada de Fourier da Onda Quadrada')
plt.xlabel('Frequência')
plt.grid(True)
plt.tight_layout()
plt.show()
