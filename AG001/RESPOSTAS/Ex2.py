#exercício 2 - AG001

import sympy as sym #Bibliotecas importadas.

c = 1445%10 #valor de C, QUE É IGUAL AO RESTO DA DIVISÃO DE 1445(MEU NÚMERO DE MATRÍCULA) POR 10.

t = sym.symbols('t')

#eq.posição
def eqposic(t):
    
    return ((-t**3)/3)+2*t**2-c

#DERIVANDO A EQUAÇÃO DA POSIÇÃO P/ OBTER A EQUAÇÃO DA VELOCIDADE
eqvelocidade = sym.diff(eqposic(t),t).doit()
print('A EQUAÇÃO DA VELOCIDADE É: {}'.format(eqvelocidade))

#VELOCIDADE EM t = 3.
velocidade = eqvelocidade.subs(t,3)
print('A velocidade em t = 3s é: {} m/s'.format(velocidade))

#DERIVANDO 2 VEZES A EQUAÇÃO DA POSIÇÃO P/ OBTER A EQUAÇÃO DA ACELERAÇÃO
eqaceler = sym.diff(eqposic(t), t, 2).doit()
print('A EQUAÇÃO DA ACELERAÇÃO É: {}'.format(eqaceler))

#ACELERAÇÃO EM t = 5.
aceler = eqaceler.subs(t,5)
print('A aceleração em t = 5s é: {} m/s^2'.format(aceler))