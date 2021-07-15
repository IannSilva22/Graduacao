USE aula;

CREATE TABLE funcionario_1 (cod INT (3) NOT NULL AUTO_INCREMENT,
                          nome VARCHAR(45) NOT NULL,
                          sexo CHAR(1) NOT NULL,
                          salalio DECIMAL (6,2) NOT NULL,
                          PRIMARY KEY (cod)
                          );

INSERT INTO funcionario_1 (nome, sexo, salalio) VALUES ('Pedro', 'M', 7820.00);
INSERT INTO funcionario_1 (nome, sexo, salalio) VALUES ('Maria', 'F', 9509.99);
INSERT INTO funcionario_1 (nome, sexo, salalio) VALUES ('João', 'M', 4050.93);
INSERT INTO funcionario_1 (nome, sexo, salalio) VALUES ('Marta', 'F', 2010.10);

SELECT * FROM funcionario_1;

DELIMITER $$
CREATE PROCEDURE func_minimo (sal DECIMAL)
SELECT COUNT(*) FROM funcionario_1 WHERE salalio < sal
$$
CALL func_minimo(10000);

DELIMITER $$
CREATE PROCEDURE func_salario (id smallint)
SELECT * FROM funcionario_1 WHERE cod = id
$$

CALL func_salario(2);

DELIMITER $$
CREATE PROCEDURE aumento()
UPDATE funcionario_1 SET salalio = (salalio * 1.1) WHERE cod > 0
$$

call aumento()

SELECT * FROM funcionario_1;

UPDATE funcionario_1 SET salalio = 5000 WHERE cod = 2;

DROP PROCEDURE func_salario;


DELIMITER $$
CREATE FUNCTION soma(a INT, b INT)
RETURNS INT
RETURN a + b
$$

SELECT soma(3, 4);


