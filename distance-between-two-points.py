import numpy as np

# Definir as coordenadas dos pontos P(x1, y1) e Q(x2, y2)
P = np.array([1, 2])
Q = np.array([4, 6])

# Calcular a distância
distancia = np.linalg.norm(Q - P)
print(f"A distância entre os pontos P e Q é: {distancia}")
