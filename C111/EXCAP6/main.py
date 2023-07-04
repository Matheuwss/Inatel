#EXERCÍCIOS CAP.6
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#CARREGANDO OS DATASET'S
paisesDS = pd.read_csv("paises.csv", delimiter=";")
spaceDS = pd.read_csv("space.csv", delimiter=";")

#1- POR MEIO DO DATASET SPACE.CSV, TRACE UM GRÁFICO EM BARRAS MOSTRANDO QUANTAS EMPRESAS ESPACIAIS OS EUA E A CHINA POSSUEM;
CHINA = pd.unique(spaceDS['Company Name'][spaceDS['Location'].str.contains('China')])
EUA = pd.unique(spaceDS['Company Name'][spaceDS['Location'].str.contains('USA')])

#PLOTANDO O GRÁFICO (EM BARRAS)
eixoX = ['EUA', 'CHINA']
eixoY = [len(EUA), len(CHINA)]
plt.bar(eixoX, eixoY, color='cyan')
plt.title('NÚMERO DE EMPRESAS ESPACIAIS DOS EUA E CHINA')
plt.show()


#2- POR MEIO DO DATASET PAISES.CSV, TRACE DOIS GRÁFICOS DE LINHAS EM UMA MESMO PLANO CARTESIANO. UM MOSTRANDO A TAXA DE MORTALIDADE (DEATHRATE) E OUTRO A TAXA DE
#NATALIDADE (BIRTHRATE) DOS PAÍSES DA AMÉRICA DO NORTE (NORTHERN AMERICA);
info = paisesDS[['Country', 'Deathrate', 'Birthrate']][paisesDS['Region'].str.contains('NORTHERN AMERICA')]

plt.plot(info['Country'], info['Deathrate'], 'o-r', info['Country'], info['Birthrate'], 'o-b')
plt.title('TAXA DE MORTALIDADE E NATALIDADE DOS PAÍSES DA AMÉRICA DO NORTE')
plt.show()
