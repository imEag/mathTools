import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def model(y, t):
    k = 0.3
    dydt= -k * y
    return dydt

#condicion inicial
y0 = 5

#tiempo para la grafica
t=np.linspace(0,100)

#solucionar ODE
y = odeint(model, y0, t)

#graficar
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
