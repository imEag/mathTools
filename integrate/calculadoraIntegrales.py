import sympy as sym

t = sym.Symbol('t')
s = sym.Symbol('s')
x = sym.Symbol('x')

def integralIndefinida(exp, ter):
    exp = sym.parse_expr(exp)
    sol = sym.integrate(exp, (ter,))
    return sol

def integralDefinida(exp, ter, limI, limS):
    exp = sym.parse_expr(exp)
    sol = sym.integrate(exp, (ter, limI, limS))
    return sol

def mostrar(sol):
    print('\n solución de la integral: \n')
    sym.pprint(sol)
    print('\n \n')

print("""Calculadora de fracciones parciales, 
ingrese las expresiones en términos de x y/o t.\n""")
while True:
    op = input("""1. Integral indefinida. 
    2. Integral definida.
    3. Salir \n
    : """)

    if (op == '1'):
        expresion = input('Ingrese la expresión: ')
        termino = input('Ingrese el término con el que se va a integrar: ')
        sol = integralIndefinida(expresion, termino)
        mostrar(sol)
        op2 = input('1. Resolver otra integral. \n2. salir')
        if (op2 == '1'):
            pass
        else:
            break    
    elif (op == '2'):
        expresion = input('Ingrese la expresión: ')
        termino = input('Ingrese el término con el que se va a integrar: ')
        limInferior = input('Ingrese el límite interior: ')
        limSuperior = input('Ingrese el límite superior: ')
        sol = integralDefinida(expresion, termino, limInferior, limSuperior)
        mostrar(sol)
        op2 = input('1. Resolver otra integral. \n2. salir')
        if (op2 == '1'):
            pass
        else:
            break   
        
    elif (op == '3'):
        exit()
    else:
        pass