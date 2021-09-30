import sympy as sym

t = sym.Symbol('t')
s = sym.Symbol('s')
x = sym.Symbol('x')
e = sym.exp

ec = sym.sin(2*x)*sym.cos(2*(t-x))
sol = sym.integrate(ec, (x, 0, t))

print('\n integral: \n')
sym.pprint(sol)
