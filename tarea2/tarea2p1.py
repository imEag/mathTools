import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def model(P, x):
    a = ((2-(x**2))/((x**2)-x))
    b = ((2-x)/((x**2)-x))
    c = (((x-1)**2)/((x**2)-x))
    return [(P[1], b*P[0] + a*P[1] + c),(P[1], b*P[0] + a*P[1] + c)]


#cond. iniciales
p0 = [1, 0]

# eje horizontal
xs = np.linspace(2, 250,500)

# sol ODE
y = odeint(model, p0, xs)
ys=y[:,1]
#graficar
plt.plot(xs,ys)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()