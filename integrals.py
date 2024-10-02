import sympy as sp

# Definir a variável e a função
x = sp.symbols('x')
f = sp.cos(x**2)

# Calcular a integral indefinida
integral_indef = sp.integrate(f, x)
print(f"A integral indefinida de f(x) = exp(-x^2) é: {integral_indef}")

# Calcular a integral definida de -∞ a ∞
integral_def = sp.integrate(f, (x, -sp.oo, sp.oo))
print(f"A integral definida de f(x) de -∞ a ∞ é: {integral_def}")
