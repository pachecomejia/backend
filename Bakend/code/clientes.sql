Drop table if exists clientes;
Create table clientes(
     id_cliente       integer primary key autoincrement,

    nombre           varchar(50) not null,
    email            varchar(50) not null,
    numero  varchar(20) not null
    );




insert into clientes(nombre,email,numero) values ("Luis","luis@icloud.com",      "7758889999");
insert into clientes(nombre,email,numero) values ("Gustabo","gustabo@icloud.com","7767777888");
insert into clientes(nombre,email,numero) values ("Kevin","kevin@icloud.com",    "7759966655");


Select * From clientes;

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios(
    username TEXT,
    password varchar(32),
    level INTEGER
);

CREATE UNIQUE INDEX index_usuario ON usuarios(username);

INSERT INTO usuarios(username, password, level) VALUES('admin','21232f297a57a5a743894a0e4a801fc3',0);
INSERT INTO usuarios(username, password, level) VALUES('user','ee11cbb19052e40b07aac0ca060c23ee',1);

SELECT * FROM usuarios;
