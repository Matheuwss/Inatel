DROP DATABASE IF EXISTS EXCAP4;
CREATE DATABASE EXCAP4;
USE EXCAP4;

#Exercício - CAP.4 (PARTE 1)
#CRIANDO TABELAS
CREATE TABLE Empregado
(
  PNome VARCHAR(15) NOT NULL,
  MInicial CHAR,
  UNome VARCHAR(15) NOT NULL,
  SSN BIGINT NOT NULL,
  DataNasc DATE,
  Endereco VARCHAR(80),
  Sexo BIT,
  Salario DECIMAL(10,2),
  SSN_Supervisor BIGINT,
  DNumero_Departamento INT NOT NULL,
  
  PRIMARY KEY (SSN),
  CONSTRAINT fk1
	FOREIGN KEY (SSN_Supervisor) REFERENCES empregado (SSN) 
    ON DELETE SET NULL ON UPDATE CASCADE,
  
  CONSTRAINT fk2
	FOREIGN KEY (DNumero_Departamento) REFERENCES departamento (DNumero)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Departamento
(
    DNome VARCHAR(15) NOT NULL,
    DNumero INT NOT NULL AUTO_INCREMENT,
    SSN_Empregado BIGINT,
    DataInicio DATE,
    
	PRIMARY KEY (DNumero),
	CONSTRAINT fk1
		FOREIGN KEY (SSN_Empregado) REFERENCES Empregado (SSN)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE DEPTO_LOCALIZACOES
(
	LNumero INT NOT NULL,
	DLocalizacao VARCHAR(20) NOT NULL,
	DNumero_Departamento INT NOT NULL,
    
	PRIMARY KEY (LNumero),
	CONSTRAINT fk1
		FOREIGN KEY (DNumero_Departamento) REFERENCES Departamento (DNumero)
		ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Projeto
(	
	PNome VARCHAR(15) NOT NULL,
	PNumero INT NOT NULL AUTO_INCREMENT,
	PLocalizacao VARCHAR(20) NOT NULL,
	DNumero_Departamento INT NOT NULL,
    
	PRIMARY KEY (PNumero),
    CONSTRAINT fk1
		FOREIGN KEY (DNumero_Departamento) REFERENCES Departamento (DNumero)
		ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE TRABALHA_EM
(
	SSN_Empregado INT NOT NULL,
	PNumero_Projeto INT NOT NULL,
	Horas INT,
    
	PRIMARY KEY (SSN_Empregado, PNumero_Projeto),
    CONSTRAINT fk1
		FOREIGN KEY (SSN_Empregado) REFERENCES Empregado (SSN)
		ON DELETE CASCADE ON UPDATE CASCADE,
    
	CONSTRAINT fk2
		FOREIGN KEY (PNumero_Projeto) REFERENCES Projeto (PNumero)
		ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Dependente
(
	SSN_Empregado BIGINT NOT NULL,
	Nome_Dependente VARCHAR(15) NOT NULL,
	Sexo BIT,
	DataNasc DATE,
	Parentesco VARCHAR(10),
    
	PRIMARY KEY (SSN_Empregado, Nome_Dependente),
    CONSTRAINT fk1
		FOREIGN KEY (SSN_Empregado) REFERENCES Empregado (SSN)
		ON DELETE CASCADE ON UPDATE CASCADE
);

#Exercício - CAP.4 (PARTE 2)
#1) Insira dois novos registros para Departamento preenchendo apenas 3 campos possíveis.
INSERT INTO Departamento (DNome, DNumero, SNN_Empregado) VALUES 
('Administrativo', 1, '9899977766'),
('Financeiro', 2, '8998999876');

#2) Insira um terceiro registro para Departamento apenas com nome e número;
INSERT INTO Departamento (DNome, DNumero) VALUES ('Comercial', '3');

#3) Insira dois registros preenchendo apenas 5 campos e dois registros completos de Empregado.
INSERT INTO Empregado (Pnome, MInicial, UNome, SNN, Sexo) VALUES 
('Matheus', 'F', 'Henrique', '9899977766', '1'),
('Lucas', 'C', 'Martins', '8998999876', '1');

INSERT INTO Empregado VALUES 
('Adrieli', 'R', 'Matos', '4897340039', '01/03/1998', 'Av. Rio Branco, 180, Centro, Rio de Janeiro', '0', '3400', 9899977766, '1'),
('Paulo', 'N', 'Castro', '3823489423', '12/08/1996', 'Av. Paulista, 300, Centro, São Paulo', '1', '4000', null, '3');

#4) Insira três novos registros para Projeto preenchendo apenas nome e número.
INSERT INTO Projeto (PNome, PNumero) VALUES 
('Gerenciamento Remoto de Equipamentos', '1'),
('Software de Reconhecimento Facial', '2'),
('Editais Publicos', '3');

#5) Atualize quem é o supervisor de 3 empregados que foram cadastrados.
UPDATE Empregado SET SSN_Supervisor = '3823489423' WHERE SSN = '9899977766';
UPDATE Empregado SET SSN_Supervisor = '3823489423' WHERE SSN = '8998999876';
UPDATE Empregado SET SSN_Supervisor = '8998999876' WHERE SSN = '4897340039';

#6) Atualize quem é o gerente de cada um dos Departamentos que foram cadastrados.
UPDATE Departamento SET SSN_Empregado = '9899977766' WHERE DNumero = '1';
UPDATE Departamento SET SSN_Empregado = '4897340039' WHERE DNumero = '2';
UPDATE Departamento SET SSN_Empregado = '3823489423' WHERE DNumero = '3';

#7) Atualize a localização e o departamento de cada projeto cadastrado;
UPDATE Projeto SET PLocalizacao = 'Rio de Janeiro', DNumero_Departamento = '1' WHERE PNumero = '1';
UPDATE Projeto SET PLocalizacao = 'São Paulo', DNumero_Departamento = '3' WHERE PNumero = '2';
UPDATE Projeto SET PLocalizacao = 'São Paulo', DNumero_Departamento = '1' WHERE PNumero = '3';

#8) Exclua todos os projetos que pertençam a um determinado departamento especifico.
DELETE FROM Projeto WHERE DNumero_Departamento = '3';


#Exercício - CAP.4 (PARTE 3)
#1) Busque os diferentes tipos de parentesco cadastrados na tabela Dependente
SELECT Parentesco FROM Dependente;

#2) Busque o último nome e data de nascimento de todos os empregados que são do sexo masculino e ordene os resultados pela data de nascimento (dos mais velhos para os mais novos)
SELECT UNome, DataNasc FROM Empregado WHERE Sexo = '1' ORDER BY DataNasc DESC;

#3) Busque o nome de cada dependente juntamente com o primeiro nome do seu responsável
SELECT D.Nome_Dependente, E.PNome FROM Dependente AS D, Empregado AS E WHERE D.SSN_Empregado = E.SSN;

#4) Busque a média salarial de todos os empregados da empresa que residem na cidade de São Paulo e trabalham no departamento de Engenharia
SELECT AVG(emp.Salario) AS 'MÉDIA SALARIAL' FROM Empregado AS emp, Departamento AS depto WHERE emp.Endereco = 'São Paulo' AND depto.DNome = 'Engenharia' AND depto.SSN_Empregado = emp.SSN;

#5) Para cada supervisor, busque seu primeiro nome, o primeiro nome dos empregados que ele gerencia e a diferença salarial do salário dele para cada um de seus empregados
SELECT sup.PNome, emp.PNome, (sup.Salario - emp.Salario) AS 'DIFERENÇA SALARIAL' FROM Empregado AS sup, Empregado AS emp WHERE emp.SSN_Supervisor = sup.SSN;

#6) Para cada empregado, busque seu primeiro nome, o nome dos projetos que ele trabalha e o número de horas em cada projeto
SELECT emp.PNome, proj.PNome, trab_em.Horas FROM Empregado AS emp, Projeto AS proj, TRABALHA_EM AS trab_em WHERE trab_em.SSN_Empregado = emp.SSN AND trab.PNumero_Projeto = proj.PNumero;