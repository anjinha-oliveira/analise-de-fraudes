# analise de fraudes

Esse projeto consiste em analisar transações fraudulentas de cartões de crédito através dos arquivos de  “clients” e “transactions”.
A primeira coisa a ser feita é adicionar os arquivos de “clients” e “transactions” em uma pasta no VSCode, após isso vou criar um Database no SQL chamada "Fraudes", em seguida vou criar também as tabelas "Clientes" e "Transacoes" no banco de dados "Fraudes".
 
Vou fazer uma aplicação para processar esses arquivos usando Python, após processar todos os arquivos "clients" e "transaction" no VSCode, vou fazer a conexão no banco de dados inserindo os arquivos em suas devidas tabelas.
 
 Após inserir esses arquivos em suas devidas tabelas no banco de dados relacional, vou analisar esses arquivos para descobrir quais transações são fraudulentas.
As fraudes são as que tiverem transações abaixo de 2 minutos de espaçamento.

# Para criar o banco de dados:

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
```

Essas tabelas vão receber os dados dos documentos “clients” e “transactions”
