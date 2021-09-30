import sympy as sym

# INGRESO
t = sym.Symbol('t')
uH = sym.Heaviside
e=sym.exp
pi=sym.pi
#ec = sym.exp(-1*t)*sym.sin(t)*uH(t-sym.pi)
#el anterioir no funciona, hay que reescribirlo
ec= -1*e(-1*pi)*e(-1*(t-pi))*sym.sin(t-pi)*uH(t-pi)
# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec,t,s)

# SALIDA
print('\n f(t) = (3t+1*u(t-1)) \n')
print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)