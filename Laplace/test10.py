import sympy as sym

# INGRESO
t = sym.Symbol('t')
a = sym.pi
uH = sym.Heaviside
ec = (1-sym.cos(t))*uH(t)

# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec, t, s)

# SALIDA
print('\n f(t) = cos(t-a)*u(t-a) \n')
print('ecuation \n:')
sym.pprint(ec)
print('ecuation Solved: \n')
sym.pprint(ecS)
