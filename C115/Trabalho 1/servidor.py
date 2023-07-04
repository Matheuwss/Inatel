from socket import *

#DEFINE O ENDEREÇO E A PORTA EM QUE O SERVIDOR VAI FICAR ESCUTANDO.
server_end = 'localhost'
server_port = 4000

#CRIA O SOCKET DO SERVIDOR E O VINCULA COM O ENDEREÇO E A PORTA DEFINIDOS.
server = socket(AF_INET, SOCK_STREAM)
server.bind((server_end, server_port))

#COLOCA O SOCKET DO SERVIDOR EM MODO DE ESCUTA (COM NO MÁXIMO UM CLIENTE NA FILA).
server.listen(1)

#IMPRIME A MENSAGEM INDICANDO QUE O SERVIDOR ESTÁ PRONTO P/ RECEBER CONEXÕES
print(f"Servidor escutando em {server_end}:{server_port}...")
print("Aguardando conexão de um cliente.")

#LOOP PRINCIPAL DO SERVIDOR
while True:
    #AGUARDA UMA CONEXÃO
    connection, end_cliente = server.accept()
    print("Cliente conectado!!\n")

    #RECEBE O NOME DO ARQUIVO SOLICITADO PELO CLIENTE (em bytes)
    nome_arquivo = connection.recv(1024).decode()

    #ABRE O ARQUIVO E ENVIA O CONTEÚDO P/ O CLIENTE
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo_arquivo = arquivo.read()
            connection.send(conteudo_arquivo.encode())
            print(f"Enviando o conteúdo do arquivo {nome_arquivo} p/ {end_cliente}...")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")

    #FECHA A CONEXÃO
    connection.close()
    