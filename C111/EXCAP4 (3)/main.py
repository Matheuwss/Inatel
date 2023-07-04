#EXERCÍCIOS CAP.4 (PT3)
import numpy as np

spaceDS = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')           #Importando o dataset space.csv

#1- APRESENTE A PORCENTAGEM DE QUANTAS MISSÕES DERAM CERTO;
success = np.count_nonzero(spaceDS[1:, 7] == "Success")
linhas, colunas = spaceDS.shape

PORCENTAGEM = (success / (linhas - 1)) * 100
print("Q1) Porcentagem das missões que deram certo:", PORCENTAGEM, "%\n")



#2- QUAL A MÉDIA DE GASTOS DE UMA MISSÃO ESPACIAL SE BASEANDO EM MISSÕES QUE POSSUAM VALORES DISPONIVEIS (> 0);
arr1 = spaceDS[1:, 6].copy().astype(float)          #Pegando os gastos das missões - COLUNA 6 (como CÓPIA) --- E mudando o tipo do arr p/ float.
arr2 = (arr1[arr1 > 0])                             #REMOVENDO OS ELEMENTOS <= 0
print("Q2) MÉDIA DE GASTOS DAS MISSÕES (>0):", arr2.mean(), "\n")



#3- ENCONTRE QUANTAS MISSÕES ESPACIAIS NESTE DATASET FORAM REALIZADAS PELOS ESTADOS UNIDOS (EUA);
arr3 = spaceDS[1:, 2]                               #Salvando no arr3 apenas as missões (COLUNA 2)
indices = np.char.find(arr3, "USA")                 #Pegando (PARA CADA ELEMENTO DO ARR DE MISSÕES) o índice em que a substring "USA" aparece
resp = np.count_nonzero(indices > -1)               #Pegando/contando os ínidces que são maiores que -1
print("Q3) MISSÕES ESPACIAIS QUE FORAM REALIZADAS PELOS ESTADOS UNIDOS:", resp, "\n")

#OU, fazendo:
#EUA = np.sum(np.char.count(spaceDS[1:, 2], 'USA'))
#print(EUA)




#4- ENCONTRE QUAL FOI A MISSÃO MAIS CARA REALIZADA PELA EMPRESA "SPACEX"
indicesx = np.where(spaceDS == "SpaceX")            #Pegando os índices das linhas onde "SpaceX" aparece
arr4 = spaceDS[indicesx[0]]                         #Criando um novo arr (SÓ COM AS LINHAS DESEJADAS) ---- USA-SE [0] P/ PEGAR O PRIMEIRO ÍNDICE DA TUPLA RETORNADA PELA FUNÇÃO WHERE
MAX = arr4[0:, 6].astype(float).max()               #Pegando os gastos (COLUNA 6) do arr4, mudando o tipo e selecionando o valor máximo.
print("Q4) MISSÃO MAIS CARA REALIZADA PELA SPACEX:", MAX, "\n")



#5- MOSTRE O NOME DAS EMPRESAS QUE JÁ REALIZARAM MISSÕES ESPACIAIS JUNTAMENTE COM SUAS RESPECTIVAS QUANTIDADES DE MISSÕES
#(USE O FOR NO FINAL PARA MOSTRAR AS INFORMAÇÕES).
print("Q5) NOME DAS EMPRESAS JUNTAMENTE COM SUAS RESPECTIVAS QUANTIDADES DE MISSÕES:")
nomes = spaceDS[1:, 1]    #Pegando o nome das empresas.
nomes, x = np.unique(nomes, return_counts=True)
for i in range(len(nomes)):
    print(nomes[i], '=', x[i])
