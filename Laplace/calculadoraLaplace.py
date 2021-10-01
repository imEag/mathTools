import sympy as sym

t = sym.Symbol('t')
s = sym.Symbol('s')
x = sym.Symbol('x')
uH = sym.Heaviside


def laplace(exp):
    exp = sym.parse_expr(exp)
    sol = sym.laplace_transform(exp, t, s)
    return sol

def laplace_inversa(exp):
    exp = sym.parse_expr(exp)
    sol = sym.inverse_laplace_transform(exp, s, t)
    return sol

def mostrar(exp):
    print('\n ecuation solved: \n')
    sym.pprint(exp)

print("""Calculadora de Laplace normal e inversa.
\n""")
while True:
    op = input("""1. Laplace.
2. Laplace inversa.
3. Salir \n
    : """)

    if (op == '1'):
        print('Para escribir un escalon unitario u(t) escriba Heaviside(aquí va el argumento), ejemplo: Heaviside(t-1). \n')
        expresion = input(
            'Ingrese la expresión (ingrese las expresiones en términos de t): ')
        sol = laplace(expresion)
        mostrar(sol)
        op2 = input('1. Resolver otra expresión. \n2. salir  \n:  ')
        if (op2 == '1'):
            pass
        else:
            break
    elif (op == '2'):
        expresion = input('Ingrese la expresión (ingrese las expresiones en términos de s): ')
        sol = laplace_inversa(expresion)
        mostrar(sol)
        op2 = input('1. Resolver otra expresión. \n2. salir  \n: ')
        if (op2 == '1'):
            pass
        else:
            break

    elif (op == '3'):
        exit()
    else:
        pass
