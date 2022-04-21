# analise de fraudes

Esse projeto consiste em analisar transações fraudulentas de cartões de crédito através dos arquivos de  “clients” e “transaction”.
A primeira coisa a ser feita é adicionar os arquivos de “clients” e “transaction” em uma pasta no VSCode, após isso vou criar um Database no SQL chamada "Fraudes", em seguida vou criar também as tabelas "Clientes" e "Transacoes" no banco de dados "Fraudes".
 
Vou fazer uma aplicação para processar esses arquivos usando Python, após processar todos os arquivos "clients" e "transaction" em python, vou fazer a conexão no banco de dados inserindo os arquivos em suas devidas tabelas.
 
 Após inserir esses arquivos em suas devidas tabelas no banco de dados relacional, vou analisar esses arquivos para descobrir quais transações são fraudulentas.
As fraudes são as que tiverem transações abaixo de 2 minutos de espaçamento.

# Configuração do banco de dados

Sintaxe para criar o banco de dados:

```sql
Create database Fraudes;
```

Após criar o banco, execute:

```sql
Use Fraudes
Go
```

Para executar todos os meus comandos dentro do banco de dados Fraudes.

Para criar as tabelas dentro do banco:

```sql
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
```

Essas tabelas vão receber os dados dos documentos “clients” e “transaction”

# Como executar 

Primeiramente criei um script para listar todos os arquivos de "clients" ultilizando
a biblioteca "os"

```python

import os

```
Após importar a biblioteca, adicionei o caminho do diretorio na variavel "pasta"

``` python

pasta = './arquivos-para-analise'

```

Utilizei a função "os.walk()" para varrer todo o caminho do diretorio 
e delimitei os arquivos que deveriam ser exibidos dentro do meu diretorio com o "if".
O "sorted()" utilizei para exibir os arquivos de forma ordenada

```python

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if 'clients' in arquivo:
			print(arquivo)
```
A saida esperada será

```py 

$ python importar-dados.py
clients-001.csv
clients-002.csv
clients-003.csv
clients-004.csv

```