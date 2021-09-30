import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Definicion de E.D a resolver: y''+x*y'+20*sin(y)=0
def df(y,x):
    y1, y2= y[0], y[1] #variables de paso
    dy1=y2  # derivada variable 1
    dy2=-x*y2-20*np.sin(y1) # derivada variable 2
    return [dy1,dy2]

# Condiciones iniciales 
y0 =[0,1]

# Definicion del rango 
x = np.linspace(0,6,500)

# Para mayor info: help(odeint)
# solucion numerica
sol = odeint(df, y0, x)
y=sol[:,0] #toma el vector correspondiente a la solucion de y1
plt.plot(x,y)
plt.show()