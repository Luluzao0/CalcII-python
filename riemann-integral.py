import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import sin, cos
from mpl_toolkits.mplot3d import Axes3D

def integral_riemann(expr, var, a, b, num_rectangles=1000):
    x = sp.symbols(var)
    dx = (b - a) / num_rectangles
    integral_sum = 0

    for i in range(num_rectangles):
        xi = a + i * dx
        integral_sum += expr.subs(x, xi) * dx

    return integral_sum

def plot_2d(expr, var, a, b, num_rectangles=1000):
    x = np.linspace(a, b, num_rectangles)
    y = np.array([float(expr.subs(var, xi)) for xi in x])

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ax.fill_between(x, y, alpha=0.2)
    ax.set_title(f'Integral Indefinida de {expr} no intervalo [{a}, {b}]')
    ax.set_xlabel(var)
    ax.set_ylabel('Função')

    plt.show()

def plot_3d(expr, var, a, b, num_rectangles=100):
    x = np.linspace(a, b, num_rectangles)
    y = np.array([float(expr.subs(var, xi)) for xi in x])
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)  # Inicializa a matriz Z com zeros, pois a altura é zero

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

    ax.set_title(f'Área sob a curva de {expr} no intervalo [{a}, {b}]')
    ax.set_xlabel(var)
    ax.set_ylabel('Função')
    ax.set_zlabel('Z')

    plt.show()

def main():
    # Exemplo: Calcular a integral indefinida de x^2 em relação a x no intervalo [0, 1]
    x = sp.symbols('x')
    expression = cos(x**2)

    a = 1
    b = 2
    
    result_riemann = integral_riemann(expression, 'x', a, b)
    result_sympy = sp.integrate(expression, (x, a, b))

    print(f"Resultado usando Riemann: {result_riemann}")
    print(f"Resultado usando Sympy: {result_sympy}")

    plot_2d(expression, x, a, b)
    plot_3d(expression, x, a, b)

if __name__ == "__main__":
    main()
