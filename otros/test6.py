import sympy as sp
from sympy import *
from sympy.interactive import printing
printing.init_printing(use_latex=True)


x = sp.Symbol('x')
f = sp.Function('f')(x)

ec = Eq(f.diff(x),x**2)
print(ec)


sol = dsolve(ec, f)
print(sol)
