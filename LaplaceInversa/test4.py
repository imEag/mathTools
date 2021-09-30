import sympy as sym

# INGRESO
s = sym.Symbol('s')
a = sym.pi
uH = sym.Heaviside
ec = 1 / (1 + (s+1)**2)

# PROCEDIMIENTO
# Transformando a Laplace
t = sym.Symbol('t')
ecS = sym.inverse_laplace_transform(ec, s, t)

# SALIDA

print('ecuation \n:')
sym.pprint(ec)
print('ecuation Solved: \n')
sym.pprint(ecS)
