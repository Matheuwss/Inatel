#AV4 de C207-L4
DROP DATABASE IF EXISTS nasa;
CREATE DATABASE nasa;
USE nasa;

SET GLOBAL log_bin_trust_function_creators = 1;
SET SQL_SAFE_UPDATES = 0;

#CRIANDO TABELAS
CREATE TABLE galaxia (
	id_galaxia INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    massa DOUBLE,
    tamanho FLOAT,
    tipo VARCHAR(20)
);

CREATE TABLE estrela (
	id_estrela INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    massa DOUBLE,
    tamanho FLOAT,
    luminosidade FLOAT,
    galaxia_id int,
    CONSTRAINT fk_galaxia
    FOREIGN KEY (galaxia_id) REFERENCES galaxia(id_galaxia) ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE planeta (
	id_planeta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    massa DOUBLE,
    tamanho FLOAT,
    habitavel BOOLEAN,
    dist_terra FLOAT,
    estrela_id int,
    CONSTRAINT fk_estrela
    FOREIGN KEY (estrela_id) REFERENCES estrela(id_estrela) ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

INSERT INTO galaxia(nome, massa, tamanho, tipo) VALUES 
('Via Lactea', 1.9*POW(10,12), '105700', 'Espiral'),
('Andrômeda', 1.23*POW(10,11), '220000', 'Espiral'), 
('Pequena Nuvem de Magalhães', 6.5*POW(10,9), '7000', 'Irregular');

INSERT INTO estrela(nome, massa, tamanho, luminosidade, galaxia_id) VALUES 
('Sol', 1.989*POW(10,30), 1.392*POW(10,6), 1, 1),
('Kepler-438', 1.082*POW(10,30), 723.84*POW(10,6), 0.044, 1), 
('Gliese 667', 1.372*POW(10,30), 974.4*POW(10,6), 0.0137, 1);

INSERT INTO planeta(nome, massa, tamanho, habitavel, dist_terra, estrela_id) VALUES
('Terra', 5.9722*POW(10,24), 12742, TRUE,0, 1),
('Kepler-438b', NULL, 14271,TRUE,470, 2), 
('Gliese 667 Cc', 2.621*POW(10,25), 19113, TRUE, 22, 3), 
('Marte', 6.4174*POW(10,22), 6779, FALSE, 3.805*POW(10,-5),1);


#QUESTÃO 1
CREATE VIEW busca AS (
	SELECT G.nome AS 'GALÁXIA', E.nome AS 'ESTRELA', P.nome AS 'PLANETA' FROM galaxia AS G, estrela AS E, planeta AS P
    WHERE E.galaxia_id = G.id_galaxia AND P.estrela_id = E.id_estrela
);

SELECT * FROM busca;


#QUESTÃO 2
DELIMITER $$
CREATE FUNCTION encontra_planeta(habitavel_planeta BOOLEAN, dist_planeta FLOAT) RETURNS VARCHAR(20)
BEGIN
    DECLARE resultado VARCHAR(20);
    
    IF habitavel_planeta = FALSE AND dist_planeta > 30 THEN
		SET resultado = 'Inabitável e longe';
	ELSEIF habitavel_planeta = FALSE AND dist_planeta < 30 THEN
		SET resultado = 'Inabitável';
	ELSEIF habitavel_planeta = TRUE AND dist_planeta > 30 THEN
		SET resultado = 'Habitável e longe';
	ELSEIF habitavel_planeta = TRUE AND dist_planeta <= 30 THEN
		SET resultado = 'Habitável e Perto';    
	END IF;
    
    RETURN resultado;

END $$
DELIMITER ;

SELECT nome AS 'Nome', encontra_planeta(habitavel, dist_terra) AS 'Resultado' FROM planeta;



#QUESTÃO 3
DELIMITER $$
CREATE PROCEDURE excluir(IN id INT, IN dist_terra FLOAT, IN habitavel BOOLEAN)
BEGIN

    IF habitavel = FALSE OR dist_terra > 30 THEN	#Se a condição for VERDADEIRA, EXCLUI O PLANETA.
		DELETE FROM planeta WHERE id_planeta = id;
	END IF;
    
	SELECT nome AS 'Nome', encontra_planeta(habitavel, dist_terra) AS 'Resultado' FROM planeta;
    
END $$
DELIMITER ;

CALL excluir(1, 0, TRUE);
CALL excluir(2, 470, TRUE);
CALL excluir(3, 22, TRUE);
CALL excluir(4, 3.805*POW(10,-5), FALSE);


#QUESTÃO 4
DELIMITER $$
CREATE TRIGGER verification BEFORE UPDATE ON estrela
FOR EACH ROW
BEGIN
	#quando ocorrer uma atualização de um registro de uma estrela e a luminosidade for igual a 0, todos os planetas que pertencem a esta estrela devem ser excluídos do banco.
	IF NEW.luminosidade = 0 THEN
		DELETE FROM planeta WHERE estrela_id = id_estrela;
	END IF;
    
END; $$
DELIMITER ;

UPDATE estrela SET luminosidade = 0 WHERE id_estrela = 1;	
CALL excluir(1, 0, TRUE);