import sympy as sp

# Definir a variável independente e a função
x = sp.symbols('x')
f = sp.Function('f')

# Definir a equação diferencial de segunda ordem
eq = sp.Eq(f(x).diff(x, x) + 2*f(x).diff(x) - 3*f(x), 0)

# Resolver a equação diferencial
solucao_geral = sp.dsolve(eq, f(x))
print(f"A solução geral da EDO é: {solucao_geral}")

# Definir condições iniciais
condicoes_iniciais = {f(0): 1, f(x).diff(x).subs(x, 0): 0}

# Solução particular com condições iniciais
solucao_particular = sp.dsolve(eq, f(x), ics=condicoes_iniciais)
print(f"A solução particular da EDO com condições iniciais é: {solucao_particular}")
