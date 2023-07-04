#exercício 5 - AG001

import sympy as sym #Bibliotecas importadas.

x = sym.symbols('x')

c = 1445%10  #valor de C, QUE É IGUAL AO RESTO DA DIVISÃO DE 1445(MEU NÚMERO DE MATRÍCULA) POR 10.

def eq1(x):
    return sym.exp(x-3) + sym.exp(x-1) + sym.exp(x) - (c+1)

def eq2(x):
    return x**4 - 4*(x**3) + 3*x - c

def eq3(x):
    return 4*sym.sin((c+1)*x) + 2

res1 = sym.solve(eq1(x))        #SOLUÇÃO EXATA
res1_aprox = res1[0].evalf()    #SOLUÇÃO APROXIMADA

res2 = sym.solve(eq2(x))        #SOLUÇÃO EXATA
res2_aprox = [res2[0].evalf(), res2[1].evalf(), res2[2].evalf(), res2[3].evalf()] #SOLUÇÃO APROXIMADA

res3 = sym.solve(eq3(x))        #SOLUÇÃO EXATA
res3_aprox = res3[0].evalf()    #SOLUÇÃO APROXIMADA

print('A SOLUÇÃO DA EQUAÇÃO 1 É: \nx = {} = {}'.format(res1[0],res1_aprox))
print('\nAS SOLUÇÕES DA EQUAÇÃO 2 SÃO: \nx = {}\nx = {}\nx = {}\nx = {}'.format(res2_aprox[0],res2_aprox[1],res2_aprox[2],res2_aprox[3]))
print('\nA SOLUÇÃO DA EQUAÇÃO 3 É: \nx = {} = {}'.format(res3[0],res3_aprox))