import sympy as sym

# INGRESO
t = sym.Symbol('t')
a = sym.pi
uH = sym.Heaviside
ec = t*(uH(t)-uH(t-1))

# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec, t, s)

# SALIDA
print('\n  \n')
print('ecuation : \n')
sym.pprint(ec)
print('ecuation Solved: \n')
sym.pprint(ecS)
