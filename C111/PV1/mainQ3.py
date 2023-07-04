import numpy as np

colors = [{"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
          {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
          {"color": "yellow", "type": "primary", "code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
          {"color": "blue", "type": "primary", "code": {"rgba": [0,0,255,1],"hex": "#00F"}}]

print("A) NOME DAS CORES PRIMÁRIAS:")
for i in range(4):
    if (colors[i]['type'] == 'primary'):
        print(colors[i]['color'])

print("B) CÓDIGO HEXADECIMAL DAS CORES COM TOM DE AZUL MÁXIMO (255):")
azul = []
for i in colors:
    if (i['code']['rgba'][2] == 255):
        azul.append(i)

for nome in azul:
    print(nome['code']['hex'])

print("C) ARRAY 1-D FORMADO APENAS PELO NOME E CÓDIGO HEXADECIMAL DE CADA COR:")
arrC = np.array(colors)
nome = arrC[0:, 0]    #Pegando o nome das cores.
cod = arrC[0:, 3]     #Pegando o código das cores.

for i in range(4):
    print(nome[i], cod[i])

print("D) ARRAY 1-D TRANSFORMADO EM UM ARRAY 2-D:")

print("E) TROQUE O NOME DE CADA COR NO ARRAY 2-D PELO SEU RESPECTIVO NOME EM PORTUGUÊS:")