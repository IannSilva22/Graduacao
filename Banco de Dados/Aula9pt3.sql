SHOW DATABASES;
USE aula;
SHOW TABLES;
INSERT INTO cidade(nome) VALUES ('Irati');
INSERT INTO cidade(nome) VALUES ('Ponta Grossa');

select * from usuario;
SELECT * FROM cidade;
update cidade set nome = 'Ponta Grossa' where codigo=2;
delete from cidade where codigo = 1;

describe usuario;

insert into usuario (senha, login) values ('3456', 'Joaquim');
insert into usuario (senha, login) values (888, 'joao');

update usuario set senha = 1234 where codigo = 2;

describe cidade;

create index cod_cidade on cidade (codigo);

create index cod_usuario on usuario (codigo);

create table resumo_cadastro (id int(4) not null auto_increment,
					          nome varchar(40) not null,    
							  sexo char(1) not null,
						      primary key(id), index cadastro (id) 
                    	     );

show tables;
describe resumo_cadastro;














