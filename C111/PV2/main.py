import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#CARREGANDO O DATASET
paisesDS = pd.read_csv("paises.csv", delimiter=";")


#QUESTÃO 1)
paisesALC = paisesDS[['Country', 'Region', 'Population', 'Area (sq. mi.)']][paisesDS['Region'].str.contains('LATIN AMER. & CARIB')]
print("Q1)\n", paisesALC, "\n")


#QUESTÃO 2)
qtdREGIOES = paisesDS['Region'].nunique()
print("Q2) Quantidade de regiões:", qtdREGIOES, "\n", "SÃO ELAS:\n", pd.unique(paisesDS['Region']), "\n")


#QUESTÃO 3)
print("Q3) TAXA MÉDIA DE ALFABETIZAÇÃO DO PLANETA:", paisesDS['Literacy (%)'].mean(), "\n")


#QUESTÃO 4)
paisesAN = paisesDS[['GDP ($ per capita)', 'Population']][paisesDS['Region'].str.contains('NORTHERN AMERICA')]
popMAX = paisesAN['Population'].max()
popMIN = paisesAN['Population'].min()
GDP_MAX = paisesAN['GDP ($ per capita)'].max()
GDP_MIN = paisesAN['GDP ($ per capita)'].min()

#PLOTANDO O GRÁFICO (EM BARRAS)
eixoX = ['PAÍS DE MAIOR POP.', 'PAÍS DE MENOR POP.']
eixoY = [GDP_MAX, GDP_MIN]
plt.bar(eixoX, eixoY, color='blue')
plt.ylabel('RENDA PER CAPITA (GDP)')
plt.title('RENDA PER CAPITA (GDP) DE DOIS PAÍSES DA AMÉRICA DO NORTE')
plt.show()