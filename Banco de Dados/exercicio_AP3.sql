CREATE TABLE funcionario (
                            funcionario_id INT (3) NOT NULL AUTO_INCREMENT,
                            nome_completo VARCHAR (250) NOT NULL,
                            email CHAR (150) NOT NULL,
                            valor_hora FLOAT NOT NULL,
                            PRIMARY KEY (funcionario_id)                      
                        );
describe funcionario;
INSERT INTO funcionario (nome_completo, email_f, valor_hora) VALUES ('Iann Oliveira Silva', 'iannoliver25@gmail.com', 100);
SELECT * FROM funcionario;
INSERT INTO funcionario(nome_completo, email_f, valor_hora) VALUES ('Eueueueueu', 'eu@gmail.com', 100.50);
ALTER TABLE funcionario CHANGE valor_hora valor_hora DOUBLE FLOAT NOT NULL;
INSERT INTO funcionario (nome_completo, email_f, valor_hora) VALUES ('jose', 'jose@gmail.com', 50.50);