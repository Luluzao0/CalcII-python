import sympy as sp

# Definir as variáveis
t = sp.symbols('t')
r = sp.Matrix([sp.sin(t), sp.cos(t), t])

# Calcular a derivada
r_prime = r.diff(t)

# Calcular a norma da derivada
norm_r_prime = r_prime.norm()

# Calcular a segunda derivada
r_double_prime = r.diff(t, t)

# Calcular a curvatura
curvatura = (r_prime.cross(r_double_prime)).norm() / (norm_r_prime**3)

print(f"A curvatura da curva paramétrica r(t) é: {curvatura}")
