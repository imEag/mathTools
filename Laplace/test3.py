import sympy as sym

# INGRESO
t = sym.Symbol('t')
uH = sym.Heaviside
ec = (3*t+1)*uH(t-1)
# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec,t,s)

# SALIDA
print('\n f(t) = e**-t * sin(t) * u(t - pi) \n')
print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)
