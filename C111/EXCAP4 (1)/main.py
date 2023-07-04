#EXERCÍCIOS CAP.4 (PT1)
import numpy as np

#1- CRIE UM ARRAY DE TAMANHO 21 COM VALORES LINEARMENTE ESPAÇADOS ENTRE 0 E 1;
arr0 = np.linspace(0,1,21)
print("QUESTÃO1:",arr0,"\n")


#2- CRIE DOIS ARRAYS: UM DE NÚMEROS PARES DE 0 ATÉ 51 E OUTRO TAMBÉM DE NÚMERO PARES DE 100 ATÉ 50. EM SEGUIDA, OS CONCATENE E MONSTRE O RESULTADO ORDENADO;
arr1 = np.arange(0,51,2)
arr2 = np.arange(100,50,-2)
arr3 = np.concatenate((arr1,arr2))
print("QUESTÃO2:",np.sort(arr3),"\n")


#3- ORDENE OS RESULTADOS DO ARRAY RESULTANTE DA QUESTÃO 2 EM ORDEM DECRESCENTE;
arr4 = np.flip(np.sort(arr3))
print("QUESTÃO3:",arr4,"\n")


#4- CRIE UMA MATRIZ FORMADA SOMENTE POR 1's E DE TAMANHO 3X4. EM SEGUIDA, TRANSFORME-A EM UM ARRAY 1-D;
print("QUESTÃO4:")
mtz = np.ones(12)
mtz = mtz.reshape(3,4)
print(mtz.astype(int),"\n")

array1D = mtz.reshape(-1)
print(array1D.astype(int),"\n")


#5- CRIE UMA MATRIZ DE TAMANHO QUALQUER. EXTAIA SEU NÚMERO DE LINHAS E COLUNAS, MULTIPLIQUE-OS, E DIGA SE ESTA MATRIZ PODERIA SE TORNAR UM VETOR COM NÚMERO PAR OU ÍMPAR DE ELEMENTOS;
print("QUESTÃO5:")
matriz = np.zeros((3,3))

nlinhas = np.size(matriz, 0)
ncolunas = np.size(matriz, 1)
nelementos = nlinhas * ncolunas

if nlinhas > 0 and ncolunas > 0:
    if nelementos % 2 == 0:
        print("A MATRIZ PODE SE TORNAR UM VETOR COM NÚMERO PAR DE ELEMENTOS")
    else: print("A MATRIZ PODE SE TORNAR UM VETOR COM NÚMERO ÍMPAR DE ELEMENTOS")
else: print("A MATRIZ NÃO PODE SE TORNAR UM VETOR")
