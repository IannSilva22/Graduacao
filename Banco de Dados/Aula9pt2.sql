USE aula;

SELECT * FROM cidade;
SELECT * FROM usuario;

GRANT ALL PRIVILEGES ON aula.cidade TO gerencia@localhost;

GRANT ALL privileges on aula.* to gerencia@localhost;

revoke all privileges on aula.* from gerencia@localhost;

drop user gerencia@localhost;
grant select on aula.* to gerencia@localhost;