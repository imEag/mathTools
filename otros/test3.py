import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def model(y, t, k):
    dydt = -k * y
    return dydt


# condicion inicial
y0 = 5

# tiempo para la grafica
t = np.linspace(0, 100)

# solucionar ODE
k = 0.1
y1 = odeint(model, y0, t, args=(k,))
k = 0.3
y2 = odeint(model, y0, t, args=(k,))
k = 0.5
y3 = odeint(model, y0, t, args=(k,))

# graficar
plt.plot(t, y1, 'r-', label='k=0.1')
plt.plot(t, y2, 'b-', label='k=0.3')
plt.plot(t, y3, 'g-', label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
