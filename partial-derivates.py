import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Definimos a função
def f(x, y):
    return 16 - 4 * x**2 - y**2

# Calculamos as derivadas parciais
def df_dx(x, y):
    return -8 * x

def df_dy(x, y):
    return -2 * y

# Ponto para avaliação
x_ponto = 1
y_ponto = 2

# Calculamos as derivadas no ponto (1, 2)
fx = df_dx(x_ponto, y_ponto)
fy = df_dy(x_ponto, y_ponto)

# Criamos uma grade de pontos para x e y
x = np.arange(-3, 3, 0.1)
y = np.arange(-3, 3, 0.1)
X, Y = np.meshgrid(x, y)

# Calculamos os valores de z usando a função
Z = f(X, Y)

# Criamos o contorno em 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.contour(X, Y, Z, 10, cmap='viridis')

# Plotamos a função
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5, rstride=100, cstride=100)

# Plotamos o ponto (1, 2)
ax.scatter(x_ponto, y_ponto, f(x_ponto, y_ponto), color='black', marker='o', label='Ponto (1, 2)')

# Plotamos as derivadas parciais
ax.quiver(x_ponto, y_ponto, f(x_ponto, y_ponto), fx, fy, 0, color='red', label='Derivadas Parciais')

# Adicionamos uma legenda
ax.legend(loc='upper right')

# Adicionamos rótulos aos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Exibimos o gráfico em 3D
plt.show()
