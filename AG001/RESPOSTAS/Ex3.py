#exercício 3 - AG001

import sympy as sym #Bibliotecas importadas.

c = 1445%10 #valor de C, QUE É IGUAL AO RESTO DA DIVISÃO DE 1445(MEU NÚMERO DE MATRÍCULA) POR 10.

x = sym.symbols('x')

def f(x):
    return x**3 - 4*x**2 + 5*x - c

A = sym.integrate(f(x), (x, 0, 5))

print('A ÁREA SOB A CURVA DA FUNÇÃO É: {}'.format(A))