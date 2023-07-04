#QUESTÃO 2
import numpy as np

arr1 = np.array(['Matheus', 'Pedro', 'Gabriele', 'João'])
arr2 = np.array(['Beatriz', 'Lucas', 'Marcos', 'Adriel'])

arr3 = np.concatenate((arr1,arr2))  #Concatenando os arr's 1 e 2.
arr3 = arr3.reshape(2, 4)           #Transformando o arr concatenado em um arr 2-D com mais colunas(4) do que linhas(2)
arr4 = np.flip(np.sort(arr3))       #Ordenando em ordem decrescente
print(arr4)