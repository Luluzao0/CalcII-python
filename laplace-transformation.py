import sympy as sp

# Definir a variável e a função
t, s = sp.symbols('t s')
f = sp.Function('f')(t)

# Definir a equação diferencial
eq = sp.Eq(f.diff(t, t) - 4*f, sp.DiracDelta(t - 1))

# Aplicar a transformada de Laplace
F_s = sp.laplace_transform(eq.lhs, t, s)[0]
rhs_s = sp.laplace_transform(eq.rhs, t, s)[0]

# Resolver a equação no domínio de Laplace
F_s_sol = sp.solve(F_s - rhs_s, sp.laplace_transform(f, t, s))
print(f"Solução no domínio de Laplace: {F_s_sol}")

# Aplicar a inversa de Laplace para voltar ao domínio do tempo
f_sol = sp.inverse_laplace_transform(F_s_sol, s, t)
print(f"Solução final no domínio do tempo: {f_sol}")
