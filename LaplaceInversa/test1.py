import sympy as sym

# INGRESO
s = sym.Symbol('s')
uH = sym.Heaviside
""" ec = 1 / (s**3 + s) """
ec = ((1/s**2) - (sym.exp(-s)/s**2) - (sym.exp(-s)/s)) * (1/(s+2))

# PROCEDIMIENTO
# Transformando a Laplace
t = sym.Symbol('t')
ecS = sym.inverse_laplace_transform(ec, s, t)

# SALIDA

print('ecuation \n:')
sym.pprint(ec)
print('ecuation Solved: \n')
sym.pprint(ecS)
