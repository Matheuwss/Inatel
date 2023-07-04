#exercício 1 - AG001

import sympy as sym #Bibliotecas importadas.

c = 1445%10 #valor de C, QUE É IGUAL AO RESTO DA DIVISÃO DE 1445(MEU NÚMERO DE MATRÍCULA) POR 10.

x = sym.symbols('x')

def f(x):
    return (3*(x**3) - 3)*(c+1)/(4*(x**2) - 4)

#limite p/ x -> 1
limite1 = sym.limit(f(x),x,1)
print('O limite para x -> 1 é {}'.format(limite1))

#limite p/ x -> oo
limite2 = sym.limit(f(x),x,sym.oo)
print('O limite para x -> oo é {}'.format(limite2))

#limite p/ x -> -oo
limite3 = sym.limit(f(x),x,-sym.oo)
print('O limite para x -> -oo é {}'.format(limite3))