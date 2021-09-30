import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def model(theta, x):
    a = 9.089
    b = 1.212
    c = 0.605
    d = 8.484
    """ return [P[1],-a*P[0]+b*P[1]] """
    theta1, theta2= theta[0], theta[1] #variables de paso
    dtheta1=theta2  # derivada variable 1
    dtheta2= -a*theta1# derivada variable 2
    return [dtheta1,dtheta2]


#cond. iniciales
p0 = [0.51, 0.151]

# eje horizontal
xs = np.linspace(0, 100, 200)

# sol ODE
y = odeint(model, p0, xs)
ys = y[:, 1]
# graficar
plt.plot(xs, ys)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
