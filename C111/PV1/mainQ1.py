#QUESTÃO 1
list = []
x = input("ADICIONAR UMA NOVA MÚSICA? S/N\n")

if(x == 'S'):
    while(x != 'N'):
        nome = input("NOME DA MÚSICA:")
        ano = input("ANO DA MÚSICA:")
        list.append({'MÚSICA': nome, 'ANO': ano})  #Guardando os dados (DE CADA MÚSICA) EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA.
        x = input("CONTINUAR ADICIONANDO NOVAS MÚSICAS? S/N\n")


print("A) QUANTAS MÚSICAS FORAM CADASTRADAS:", len(list))

AnoMaisAntigo = 9999
for i in range(len(list)):
    if int(list[i]['ANO']) < AnoMaisAntigo:
        AnoMaisAntigo = int(list[i]['ANO'])

print("B) INFORMAÇÕES DA(S) MÚSICAS(S) DO ANO MAIS ANTIGO:")
for i in range(len(list)):
    if int(list[i]['ANO']) == AnoMaisAntigo:
        print(list[i])