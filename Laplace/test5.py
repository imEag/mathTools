import sympy as sym

# INGRESO
t = sym.Symbol('t')
uH = sym.Heaviside
e=sym.exp
pi=sym.pi
ec=((t / (t**(1/2)))*e(-2*t))
# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec,t,s)

# SALIDA
print('\n f(t) = (t/(t**1/2)) * e**-2t \n')
print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)