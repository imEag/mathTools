import sympy as sym


# INGRESO
t = sym.Symbol('t')
uH = sym.Heaviside
e=sym.exp
pi=sym.pi
ec=(2/3)*e(-2*t)*t**(5/2)
# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec,t,s)

# SALIDA
print('\n f(t) = ((e**-t)/t) * sin(t)**2\n')
print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)