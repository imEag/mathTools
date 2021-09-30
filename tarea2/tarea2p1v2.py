import sympy as sp
from sympy import *
from sympy.interactive import printing
printing.init_printing(use_latex=True)


x = sp.Symbol('x')
y = sp.Function('y')

a = x**2-x
b = x**2-2
c = x-2
d = (x-1)**2

ec = Eq(a*y(x).diff(x, 2)+b*y(x).diff(x)+c*y(x), 0)
print(classify_ode(ec))
sol = dsolve(ec, y(x))
print(sol)
