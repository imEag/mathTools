import sympy as sp
from sympy import *
from sympy.interactive import printing
import numpy as np
printing.init_printing(use_latex=True)


t = sp.Symbol('t')
theta1 = sp.Function('theta1')
theta2 = sp.Function('theta2')

p = np.array([[theta1(t).diff(t, 2)], [theta2(t).diff(t, 2)]])
a = np.array([[-9.089, 1.212], [0.605, -8.484]])
tv = np.array([[theta1(t)], [theta2(t)]])

ec = Eq(p, a*tv)
sol = dsolve(ec, (theta1(t), theta2(t)))
print(sol)
