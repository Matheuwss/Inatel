from socket import *

#SERVER ADDRESS - (DEFINE O ENDEREÇO E A PORTA DO SERVIDOR A SER CONECTADO).
server_end = 'localhost'
server_port = 4000

#Create an INET, STREAM socket (UPD) ----> (CRIA O SOCKET DO CLIENTE E CONECTA AO SERVIDOR).
cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((server_end, server_port))
print("Conectado!!\n")

#ENVIA O NOME DO ARQUIVO DESEJADO P/ O SERVIDOR!
nome_arquivo = str(input('Digite o nome do arquivo: '))
cliente.send(nome_arquivo.encode())

#RECEBE O CONTEÚDO DO ARQUIVO SOLICITADO
conteudo_arquivo = cliente.recv(1024).decode()


#GRAVA O CONTEÚDO EM UM NOVO ARQUIVO LOCAL
if conteudo_arquivo:
    with open(f'novo_{nome_arquivo}', 'w') as novo_arquivo:
        novo_arquivo.write(conteudo_arquivo)
        print(f"Arquivo {nome_arquivo} transferido e salvo com sucesso!")
else:
    print(f"O arquivo {nome_arquivo} não foi encontrado no servidor.")


#FECHA O SOCKET DO CLIENTE
cliente.close()
