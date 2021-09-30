import sympy as sym

t = sym.Symbol('t')
s = sym.Symbol('s')
x = sym.Symbol('x')
e = sym.exp

ec = (1/2)*sym.sin(2*x)*sym.sin(2*(t-x))
sol = sym.integrate(ec, (x, 0, t))

print('\n integral: \n')
sym.pprint(sol)
