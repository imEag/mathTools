import sympy as sym

# INGRESO
t = sym.Symbol('t')
uH = sym.Heaviside
e = sym.exp
pi = sym.pi
delta = sym.DiracDelta
ec = delta(t) + uH(t) - uH(t-1) + delta(t-1)

# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec, t, s)

# SALIDA
print('\n f(t) = (t+1)**2 * u(t-2) \n')
print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)
