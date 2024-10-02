import sympy as sp

# Definir variáveis
x, y, z = sp.symbols('x y z')

# Definir a função e os limites de integração
f = x * y * z
limites_x = (x, 0, 2)
limites_y = (y, 0, 2)
limites_z = (z, 0, 2)

# Calcular a integral tripla
integral_tripla = sp.integrate(f, limites_z, limites_y, limites_x)
print(f"A integral tripla de f(x, y, z) = x * y * z é: {integral_tripla}")
