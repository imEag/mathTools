#impulso unitario desplazado
import sympy as sym


# INGRESO
t = sym.Symbol('t')
ec = sym.DiracDelta(t-18)

# PROCEDIMIENTO
# Transformando a Laplace
s = sym.Symbol('s')
ecS = sym.laplace_transform(ec,t,s)

# SALIDA
print('\n f(t) = Dirac delta: \n')
print('\n ecuation: \n')
sym.pprint(ec)
print('\n ecuation Solved: \n')
sym.pprint(ecS)