Create database Fraudes;
Use Fraudes
Go

Create table clientes(
	ID int,
	nome varchar(200),
	email varchar(300),
	data_cadastro datetime,
	telefone int
);

Create table transacoes(
	ID int,
	cliente_id int,
	valor money,
	data datetime

);