import sympy as sp

# Definir a variável e a função
x = sp.symbols('x')
f = sp.Function('f')

# Definir a equação diferencial
eq = sp.Eq(f(x).diff(x, x) - 2 * f(x).diff(x) + f(x), 0)

# Resolver a equação diferencial
solucao = sp.dsolve(eq, f(x))
print(f"A solução da equação diferencial é: {solucao}")
