import sympy as sp

# Definir a variável original e a função
x = sp.symbols('x')
u = sp.symbols('u')
f = sp.sin(x**2)

# Definir a mudança de variáveis: u = x^2
substituicao = {x: sp.sqrt(u)}

# Calcular a integral após a substituição
integral_original = sp.integrate(f, x)
integral_substituida = sp.integrate(f.subs(x**2, u) * sp.diff(sp.sqrt(u), u), u)

print(f"Integral original de sin(x^2): {integral_original}")
print(f"Integral após substituição u = x^2: {integral_substituida}")
