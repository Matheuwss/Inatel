'''
COLEÇÕES EM PYTHON

1.TUPLAS - GUARDAM OS DADOS DENTRO DE ()
         - COLEÇÃO IMUTÁVEL

2.LISTAS - GUARDAM OS DADOS DENTRO DE []
         - COLEÇÃO MUTÁVEL

3.CONJUNTOS - GUARDAM SEUS ELEMENTOS DENTRO DE {}
            - NÃO GUARDA OS INDÍCES DOS SEUS ELEMENTOS
            - NÃO GUARDA ELEMENTOS REPETIDOS

4.DICIONÁRIOS - GUARDAM SEUS ELEMENTOS DENTRO DE {}
              - USA INDíCES CUSTOMIZÁVEIS NO PADRÃO - chave
'''


#EXERCÍCIO 1
clubes = ['MANCHESTER CITY', 'REAL MADRID', 'LIVERPOOL', 'PSG', 'BARCELONA']

print(clubes[0:3])                  #A)
print(clubes[3:5])                  #B)
print(sorted(clubes))               #C)         #clubes.sort() print(clubes)
print(clubes.index('BARCELONA'))    #D)


#EXERCÍCIO 2
l1 = {'iPhone 11', 'iPhone 12', 'Galaxy A10', 'Galaxy A12', 'Xiaomi 11 Lite'}
l2 = {'iPhone 12', 'iPhone 13', 'Galaxy S20', 'Galaxy S22', 'Xiaomi REDMI 9'}
print('LOJA 1:', l1)
print('LOJA 2:', l2)

u = l1 | l2     #União
i = l1 & l2     #Interseção

print('MODELOS NO TOTAL:', u)
print('DISPONÍVEIS EM AMBAS AS LOJAS:', i)


#EXERCÍCIO 3
nome = str(input("NOME: "))
med = float(input("MÉDIA: "))

dados = {'NOME': nome, 'MÉDIA': med}

#IF P/ VERIFICAR A SITUAÇÃO FINAL DO ALUNO
if med >= 60:
    sit = 'AP'
elif med < 30:
    sit = 'RP'
else:
    sit = 'NP3'

dados['SITUAÇÃO'] = sit
print(dados)