#EXERCÍCIOS CAP.5
import pandas as pd

#1- CARREGUE O DATASET PAISES.CSV. EM SEGUIDA, MOSTRE:
dataset = pd.read_csv("paises.csv", delimiter=";")

#A) QUAIS OS PAÍSES DA OCEANIA;
paisesOC = dataset['Country'][dataset['Region'].str.contains('OCEANIA')]
print("Q1-A) PAÍSES DA OCEANIA: \n", paisesOC, "\n")

#B) QUANTOS PAÍSES SÃO DA OCEANIA;
print("Q1-B)", paisesOC.count(), "\n")


#2- MOSTRE A MÉDIA DA TAXA DE ALFABETIZAÇÃO (Literacy (%)) DO PLANETA;
print("Q2) MÉDIA DA TAXA DE ALFABETIZAÇÃO DO PLANETA:", dataset['Literacy (%)'].mean(), "\n")


#3- ENCONTRE O NOME E A REGIÃO DO PAÍS QUE POSSUI A MAIOR POPULAÇÃO;
maiorPOP = dataset[['Country', 'Region', 'Population']].max()
print("Q3) NOME:", maiorPOP['Country'], "REGIÃO:", maiorPOP['Region'], "\n")


#4- BUSQUE O NOME DE TODOS OS PAÍSES DO DATASET QUE NÃO POSSUEM COSTA MARÍTIMA (COASTLINE (COAST/AREA RATIO) == 0) E GUARDE-OS EM UM NOVO ARQUIVO CHAMADO NOCOAST.CSV;
coastline = dataset['Coastline (coast/area ratio)']                     #Pegando a COLUNA (COASTLINE (COAST/AREA RATIO).
coast0 = dataset.loc[coastline[coastline == 0].index]                   #Pegando os índices das linhas que contém os países com COASTLINE == 0
print("Q4) PAÍSES COM COASTLINE IGUAL A ZERO: \n", coast0['Country'])

coast0['Country'].to_csv('noCoast.csv', sep=';', header=False)          #Guardando esses nomes em um novo arquivo.