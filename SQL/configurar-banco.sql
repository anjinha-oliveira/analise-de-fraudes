Create database Fraudes;
Use Fraudes
Go

Create table clientes(
	ID int Primary key  identity (1,1) not null ,
	nome varchar(200),
	email varchar(300),
	data_cadastro datetime,
	telefone int
);

Create table transacoes(
	ID int Primary key identity (1,1) not null,
	cliente_id int FOREIGN KEY REFERENCES clientes(ID),
	valor money,
	data datetime

);

SET IDENTITY_INSERT clientes ON

ALTER TABLE clientes 
  ALTER COLUMN telefone varchar(50)

select * from clientes
select count(*) from clientes

SET IDENTITY_INSERT transacoes ON
SET IDENTITY_INSERT clientes ON