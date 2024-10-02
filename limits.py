import sympy as sp
from sympy import sqrt 

# Definir a variável e a função
x = sp.symbols('x')
f = (sqrt(x**2) - 1) / (x - 1)

# Calcular o limite quando x se aproxima de 1
limite = sp.limit(f, x, 1)
print(f"O limite de f(x) quando x tende a 1 é: {limite}")
