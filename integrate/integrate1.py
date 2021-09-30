import sympy as sym

t = sym.Symbol('t')
s = sym.Symbol('s')
e = sym.exp
T = 2

ec = e(-s*t)*sym.sin(sym.pi*t)
sol = sym.integrate(ec, (t, 0, 1))

print('\n integral: \n')
sym.pprint(sol)
