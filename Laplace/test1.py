import sympy as sym

# INGRESO
t = sym.Symbol('t')
uH = sym.Heaviside
""" ec = sym.exp(-1*t)*sym.sin(t)*uH(t-sym.pi) """
ec = t*(uH(t)-uH(t-1))

# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec,t,s)

# SALIDA

print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)
