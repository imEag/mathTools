# Polos y ceros de funcion de transferencia H(s)
import sympy as sym

# INGRESO
s = sym.Symbol('s')
# Ps es numerador, Qs es denominador
Ps = 1*s**0
Qs = s**3 + s

# PROCEDIMIENTO
P = Ps.as_poly(s)
Q = Qs.as_poly(s)
# Función de transferencia
Hs = P/Q
# Raices en Numerador y Denominador
Q_raiz  = sym.roots(Q)
P_raiz  = sym.roots(P)

# fracciones parciales con raices reales
parciales = sym.apart(Hs)

# SALIDA
print('Hs: \n')
sym.pprint(Hs)
print('\n Fracciones parciales con raices reales: \n')
sym.pprint(parciales)
print('\n polos: \n', Q_raiz)