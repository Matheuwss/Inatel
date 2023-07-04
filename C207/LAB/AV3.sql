DROP DATABASE IF EXISTS artesanato;
CREATE DATABASE artesanato;
USE artesanato;

CREATE TABLE Cliente(
 cpf VARCHAR(14) NOT NULL PRIMARY KEY,
 nome VARCHAR(45) NOT NULL,
 telefone VARCHAR(45) NOT NULL
);

CREATE TABLE Produto(
 codigo INT NOT NULL PRIMARY KEY,
 nome VARCHAR(45) NOT NULL,
 tipo_madeira VARCHAR(45) NOT NULL,
 preco INT NOT NULL,
 qtd_estoque INT NOT NULL
);

CREATE TABLE Compra(
 Cliente_cpf VARCHAR(14) NOT NULL,
 Produto_codigo INT NOT NULL,
 data_compra DATE NOT NULL,
 qtd_comprada INT NOT NULL,
 taxa_entrega FLOAT NOT NULL,
 PRIMARY KEY (Cliente_cpf, Produto_codigo),
 CONSTRAINT Cliente_cpf_fk
 FOREIGN KEY (Cliente_cpf) REFERENCES Cliente(cpf) ON DELETE NO ACTION 
 ON UPDATE CASCADE,
 CONSTRAINT Produto_codigo_fk 
 FOREIGN KEY (Produto_codigo) REFERENCES Produto(codigo) ON DELETE NO ACTION
 ON UPDATE CASCADE
);

#QUESTÃO 1
#a) Adicione a coluna cep na tabela Cliente como VARCHAR(9);
ALTER TABLE Cliente ADD cep VARCHAR(9);

#b) Modifique a coluna preco da tabela Produto para FLOAT;
ALTER TABLE Produto MODIFY preco FLOAT;

#c) Remova a coluna taxa_entrega da tabela Compra;
ALTER TABLE Compra DROP COLUMN taxa_entrega;

#inserções:
INSERT INTO Cliente (cpf, nome, telefone) VALUES 
('492.441.760-25', 'Luciano', '(35)99875-5572'),
('456.841.862-03', 'Flavio', '(35)3473-8562'),
('192.041.526-14', 'Paola', '(35)3471-1519'),
('556.851.862-88', 'Aline', '(11)99822-9639');

INSERT INTO Produto (codigo, nome, tipo_madeira, preco, qtd_estoque) VALUES
(0300, 'Baleia Azul', 				'Carvalho', 29.90, 	3),
(0301, 'Moinho de Vento', 			'Ipê', 		24.90, 	2),
(0400, 'Conjunto de Banquinhos',	'Carvalho', 42, 	4),
(0500, 'Porta-chaves', 				'Goiabão', 	8.90, 	7),
(0501, 'Mini Avião', 				'Mogno', 	27.90, 	4),
(0502, 'Tronco Esculpido', 			'Goiabão', 	69.90, 	2),
(0503, 'Vaso de Flores', 			'Aroeira', 	9.90, 	4),
(0504, 'Urso Pardo', 				'Aroeira', 	28.90, 	2),
(0505, 'Peixe Dourado', 			'Ipê', 		37.90, 	2),
(0800, 'Galinha Pintada', 			'Carvalho', 11.90, 	4),
(0801, 'Flauta', 					'Mogno', 	18.90, 	2),
(0802, 'Guitarra', 					'Alder', 	1000, 	5),
(0900, 'Tábua de Corte', 			'Carvalho', 8.90, 	4);

#QUESTÃO 2
#a) Atualize o cep para '35460-153' do cliente cujo cpf é igual a '556.851.862-88';
UPDATE cliente SET cep = '35460-153' WHERE cpf = '556.851.862-88';

#b) Atualize o telefone para '(35)98834-4676' do cliente cujo cpf é igual a '492.441.760-25';
UPDATE cliente SET telefone = '(35)98834-4676' WHERE cpf = '492.441.760-25';

#c) Atualize o nome, preco e qtd_estoque para 'Banquinhos Infantis', 15.90, 12, respectivamente, do produto cujo codigo é igual a 0400;
UPDATE produto SET nome = 'Banquinhos Infantis', preco = 15.90, qtd_estoque = 12 WHERE codigo = 0400;

#QUESTÃO 3
INSERT INTO Compra (Cliente_cpf, Produto_codigo, data_compra, qtd_comprada) VALUES
('492.441.760-25', '0301', '2018-08-20', '1'),
('556.851.862-88', '0503', '2020-11-12', '2'),
('456.841.862-03', '0802', '2020-10-30', '1');

#busca no banco de dados mostrando o nome do cliente, nome do produto, a data da compra e a quantidade comprada.
SELECT C.Nome AS 'Cliente', P.Nome 'Produto', Cp.data_compra, Cp.qtd_comprada FROM Cliente AS C JOIN Produto AS P JOIN Compra as Cp 
WHERE Cp.Cliente_cpf = C.cpf AND Cp.Produto_codigo = P.codigo;

#QUESTÃO 4
#a) Crie um usuário cujo nome seja Rodrigo, defina uma senha de sua preferência e atribua todos os privilégios em todos os bancos de dados disponíveis no sistema;
CREATE USER 'Rodrigo' IDENTIFIED BY '12345678';
GRANT ALL PRIVILEGES ON *.* TO 'Rodrigo';

#b) Crie um usuário cujo nome seja Secretaria, defina uma senha de sua preferência e atribua os comandos SELECT, UPDATE, DELETE, INSERT e ALTER, com permissão somente para 
#   o banco de dados artesanato e podendo manipular todas as tabelas;
CREATE USER 'Secretaria' IDENTIFIED BY '87654321';
GRANT SELECT, UPDATE, DELETE, INSERT, ALTER ON artesanato.* TO 'Secretaria';

#c) Remova o privilégio ALTER do usuário Secretária;
 REVOKE ALTER ON *.* FROM 'Secretaria';
 
#d) Exclua o usuário Secretária;
DROP USER 'Secretaria';