#exercício 4 - AG001

import sympy as sym #Bibliotecas importadas.

c = 1445%10 #valor de C, QUE É IGUAL AO RESTO DA DIVISÃO DE 1445(MEU NÚMERO DE MATRÍCULA) POR 10. 

i1, i2, i3 = sym.symbols('i1 i2 i3')

V1 = 10 + (2 * c)
V2 = 5 + (2 * c)

# O SISTEMA DE EQUAÇÕES DO CIRCUITO É:
# i1 + i2 + i3 = 0
# 25*i1 - 10*i2 = V1
# 20*i3 - 10*i2 = V2

#RESOLVENDO O SISTEMA DE EQUAÇÕES
RESULTADO = sym.solve((25*i1 - 10*i2 - V1,- 10*i2 + 20*i3 - V2, i1 + i2 + i3), (i1, i2, i3))

print('Os valores das correntes são: {}'.format(RESULTADO))
