import sympy as sp

# Definir as variáveis
x, y = sp.symbols('x y')

# Definir o campo vetorial F = (P(x, y), Q(x, y))
P = x**2 - y**2
Q = 2*x*y

# Calcular a divergência de F
divergencia = sp.diff(Q, x) - sp.diff(P, y)
print(f"A divergência de F é: {divergencia}")

# Definir os limites da região
limites_x = (x, 0, 1)
limites_y = (y, 0, 1)

# Calcular a integral dupla
integral_verificada = sp.integrate(divergencia, limites_x, limites_y)
print(f"A integral dupla para verificar o Teorema de Green é: {integral_verificada}")
