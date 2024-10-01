import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, diff, sin, cos, lambdify, solve

# Definindo a função de duas variáveis
x, y = symbols('x y')
f_sympy = sin(x) * cos(y)
f = lambdify((x, y), f_sympy, 'numpy')

# Criando uma grade de valores para x e y
x_vals = np.linspace(-2*np.pi, 2*np.pi, 100)
y_vals = np.linspace(-2*np.pi, 2*np.pi, 100)

# Criando uma malha 2D para os valores de x e y
X, Y = np.meshgrid(x_vals, y_vals)

# Calculando os valores da função para cada par (x, y)
Z = f(X, Y)

# Escolhendo um ponto específico para calcular as derivadas parciais
x0 = np.pi
y0 = np.pi
z0 = f(x0, y0)

# Calculando as derivadas parciais
df_dx = diff(f_sympy, x)
df_dy = diff(f_sympy, y)
df_dx_value = float(df_dx.subs([(x, x0), (y, y0)]))
df_dy_value = float(df_dy.subs([(x, x0), (y, y0)]))

# Calculando o plano tangente local
a = df_dx_value
b = df_dy_value
c = z0 - a*x0 - b*y0

# Calculando os valores do plano tangente para a malha 2D
Tangent_Plane = a*X + b*Y + c

# Calculando o gradiente
gradient = np.array([df_dx_value, df_dy_value])

# Encontrando pontos críticos (máximos e mínimos locais)
critical_points = solve([df_dx, df_dy], (x, y))
valid_critical_points = [(float(point[0]), float(point[1])) for point in critical_points if point[0].is_real and point[1].is_real]
critical_values = [f(point[0], point[1]) for point in valid_critical_points]

# Plotando a função, o plano tangente, as derivadas direcionais, gradientes e pontos críticos
fig = plt.figure(figsize=(14, 8))

# Gráfico de superfície da função
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax1.set_title('Gráfico da função')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# Plano tangente, derivadas direcionais, gradientes e pontos críticos
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Tangent_Plane, cmap='viridis', alpha=0.5, edgecolors='none')
ax2.quiver(x0, y0, z0, df_dx_value, df_dy_value, 0, color='r', linewidth=2, label='Derivadas Parciais')
ax2.quiver(x0, y0, z0, gradient[0], gradient[1], 0, color='g', linewidth=2, label='Gradiente')
ax2.scatter3D(*zip(*valid_critical_points), critical_values, color='red', label='Pontos Críticos', s=50)
ax2.set_title('Plano tangente, derivadas direcionais, gradientes e pontos críticos')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x, y)')
ax2.legend()

plt.show()
