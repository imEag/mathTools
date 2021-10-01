# Polos y ceros de funcion de transferencia H(s)

import sympy as sym

# INGRESO
s = sym.Symbol('s')
e = sym.exp
# Ps es numerador, Qs es denominador

def calcular(numerador, denominador):
    # PROCEDIMIENTO
    P = numerador.as_poly(s)
    Q = denominador.as_poly(s)
    # Función de transferencia
    Hs = P/Q
    # Raices en Numerador y Denominador
    Q_raiz  = sym.roots(Q)
    P_raiz  = sym.roots(P)

    # fracciones parciales con raices reales
    parciales = sym.apart(Hs)
    return parciales, Hs, Q_raiz

def mostrar(resultado, ecuacion, polos):
    # SALIDA
    print('Hs: \n')
    sym.pprint(ecuacion)
    print('\n Fracciones parciales con raices reales: \n')
    sym.pprint(resultado)
    print('\n polos: \n', polos)

print("""Calculadora de fracciones parciales, 
ingrese las expresiones en términos de s.
\n""")

while True:
    numerador = input('ingrese el numerador: ')
    denominador = input('ingrese el denominador: ')
    numerador = sym.parse_expr(numerador)
    denominador = sym.parse_expr(denominador)

    resultado = calcular(numerador, denominador)[0]
    ecuacion = calcular(numerador, denominador)[1]
    polos = calcular(numerador, denominador)[2]

    mostrar(resultado, ecuacion, polos)
    op = input('1. Resolver otra expresión. \n2. Salir\n : ')
    if (op == '1'):
        pass
    else:
        break