# analise de fraudes
 
Esse projeto consiste em analisar transações fraudulentas de cartões de crédito através dos arquivos de  “clients” e “transaction”.
 
A primeira coisa a ser feita é adicionar os arquivos de “clients” e “transaction” em uma pasta no VSCode, após isso vou criar um Database no SQL chamada "Fraudes", em seguida vou criar também as tabelas "Clientes" e "Transacoes" no banco de dados "Fraudes".
 
Vou fazer uma aplicação para processar esses arquivos usando Python, após processar todos os arquivos "clients" e "transaction" em python, vou fazer a conexão no banco de dados inserindo os arquivos em suas devidas tabelas.
 
 Após inserir esses arquivos em suas devidas tabelas no banco de dados relacional, vou analisar esses arquivos para descobrir quais transações são fraudulentas.
As fraudes são as que tiverem transações abaixo de 2 minutos de espaçamento.

 # Páginas Web

Decidi fazer uma página web com as informações dos clientes fraudulentos.
Para isso vou usar o Flask para carregar os dados na página, mas antes de começar 
a ultilizar o framework, fiz uma tabela básica com HTML e CSS e coloquei informações
de clientes falsos nela

Adicionei as informações da página "clientes.html" que será a página que vai listar
todos os clientes fraudulentos e suas principais informações. 

![Pagina de Clientes](images/pagina-de-clientes.png)

Adicionei o link "Ver mais" em cada cliente, para que o usuário possa navegar
para a segunda página onde vai estar as informações do cliente fraudulento como 
Data e Valor das transações, depois fiz o mesmo para o arquivo "transacoes.html"

![Pagina de Clientes](images/pagina-de-transacoes.png)

Nessa página eu adicionei "Voltar" para voltar para a página inicial.


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
 
Primeiramente criei um script para listar todos os arquivos de "clients" utilizando a biblioteca "os"
 
```python
 
import os
 
```
Após importar a biblioteca, adicionei o caminho do diretório na variável "pasta"
 
``` python
 
pasta = './arquivos-para-analise'
 
```
 
Utilizei a função "os.walk()" para varrer todo o caminho do diretório e delimitar os arquivos que deveriam ser exibidos dentro do meu diretório com o "if".
O "sorted()" utilizei para exibir os arquivos de forma ordenada
 
```python
 
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if 'clients' in arquivo:
            print(arquivo)
```
A saída esperada será
 
```py
 
$ python importar_dados.py
clients-001.csv
clients-002.csv
clients-003.csv
clients-004.csv
 
```
 
Para ler todos os dados dos arquivos de "clients", importamos a biblioteca Pandas
 
```py
 
import pandas as pd
 
```
 
Fiz algumas alterações no script para carregar os dados de "clients".
Fiz a alteração da condição adicionando o "not in" e "continue" para que me retorne apenas os arquivos de "clients"
 
```py
 
for arquivo in sorted(arquivos):
    if 'clients-' not in arquivo:
        continue
 
```
 
Concatenei as variáveis "pasta" e "arquivo" dentro da variavel "caminho" para retornar apenas os arquivos "clients"
 
```py
 
caminho = f'{pasta}/{arquivo}'
 
```
 
Utilizei a função "read_csv" para facilitar a leitura dos documentos csv no Pandas
 
```py
 
df = pd.read_csv(caminho, encoding= 'LATIN-1', sep= ';')
 
```
Fiz a iteração das linhas com o "df.iterrows()"
 
```py
 
for index, row in df.iterrows():
 
```
Após isso, adicionei uma condição para o retorno de cada tipo de dados, printando os dados que estejam com todos os campos do documento "clients" preenchidos.
Fiz isso porque depois que fiz a análise, percebi que alguns dados estavam com o campo "nome" vazio
 
```py
 
if 'id' in row:
                print(f'id = {row.id}')
            if 'nome' in row:
                print(f'nome = {row.nome}')
            if 'email' in row:
                print(f'email = {row.email}')
            if 'data_cadastro' in row:
                print(f'data_cadastro = {row.data_cadastro}')  
            if 'telefone' in row:
                print(f'telefone = {row.telefone}')        
                print('')
 
```

Adicionei o "print" e o "sleep()" na linha de cima da variável "pasta" para exibir o print antes da leitura dos dados no terminal.
 
```py
 
print('Listando dados de clientes:\n')
sleep(2)
 
```

Para fazer a conexão com o banco de dados, importei a biblioteca pyodbc
 
```py
 
import pyodbc
 
```
 
Atualizei a condição para retornar apenas os dados de cada coluna.
 
```py
 
for index, row in df.iterrows():
            print(f'id = {row[0]}')
            print(f'nome = {row[1]}')
            print(f'email = {row[2]}')
            print(f'data_cadastro = {row[3]}')
            print(f'telefone = {row[4]}')        
            print('')
 
```
 
Armazenei os dados do meu banco na variável "dados_de_conexao"
 
```py
 
dados_de_conexao = (
                "Driver={SQL Server};"
                "Server=BRENO-LAPTOP;"
                "Database=Fraudes;"
            )
 
```
 
Usei a variável "conexao" para armazenar a minha conexão com o banco e printei para ficar claro que a conexão foi bem sucedida.
 
```py
 
cursor = conexao.cursor()
print('Conexão bem sucedida')
 
```
 
Adicionei o identity_insert na tabela clientes para inserir o id de cada registro da tabela "clients" e mandei inserir no banco
 
```py
 
id_on = "SET IDENTITY_INSERT clientes ON"
cursor.execute(id_on)
print('Conexão id on sucedida')
 
```
 
Agora é só inserir os dados na tabela "clientes" dentro do banco de dados
 
```py
 
sqlserver = f"""INSERT INTO clientes(id, nome, email, data_cadastro, telefone)
            VALUES('{row[0]}',  '{row[1]}', '{row[2]}', '{row[3].replace(" -0300", "")}', '{row[4]}')"""
print(sqlserver)
cursor.execute(sqlserver)
cursor.commit()
 
```
 
Após inserir os dados de clients na tabela clientes, atualizei o script para inserir os dados de transaction na tabela de transacoes do meu banco de dados
 
``` py
 
print('\n')
print('Listando arquivos de transações:\n')
sleep(2)
pasta = './arquivos-para-analise'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if "transaction-" in arquivo:
            caminho_transacoes = f'{pasta}/{arquivo}'
            df = pd.read_csv(caminho_transacoes, encoding= 'LATIN-1', sep= ';')                    
 
```
 
Faço uma consulta no meu banco para saber se o cliente_id de transações existe na tabela clientes. 
Caso a variável existe_cliente retornar vazia, o id será ignorado
 
``` py
 
for index, row in df.iterrows():
    consulta_id = f"select 1 from clientes where id = '{row[1]}'"
    cursor.execute(consulta_id)
    existe_cliente = cursor.fetchone()
    if not existe_cliente:
        print(f'Ignorando id de transacoes {row[0]}')
        continue
 
```          
 
Agora eu vou analisar se o id de transacoes já foi cadastrado no banco. 
Caso ele já esteja cadastrado, vamos ignorar
 
``` py
 
consulta_transacao = f"select 1 from transacoes where id = '{row[0]}'"
    cursor.execute(consulta_transacao)
    transacao_ja_cadastrada = cursor.fetchone()
    if transacao_ja_cadastrada:
        print(f'Ignorando transacoes {row[0]}')
        continue
 
```
 
Após fazer essas análises, abro uma nova conexão com o banco de dados
para inserir os dados dos documentos transaction na tabela de transacoes
 
``` py
 
dados_de_conexao = (
    "Driver={SQL Server};"
    "Server=BRENO-LAPTOP;"
    "Database=Fraudes;"
)
 
conexao = pyodbc.connect(dados_de_conexao)
cursor = conexao.cursor()
id_on = "SET IDENTITY_INSERT transacoes ON"
cursor.execute(id_on)
transacoes = f"""INSERT INTO transacoes(id, cliente_id, valor, data)
            VALUES('{row[0]}',  '{row[1]}', '{row[2]}', '{row[3].replace(" -0300", "")}')"""
cursor.execute(transacoes)
cursor.commit()
print(f'Transação id = {row[0]}, inserido com sucesso')
 
```

A análise proposta do projeto é descobrir clientes que tem transações fraudulentas.
Essas transações fraudulentas tem um espaçamento entre uma e outra de 2 minutos. 

Depois de pesquisar formas de fazer a análise proposta do projeto, decidi fazer essa consulta no SQL Server
Para vitar que a consulta retorne dados duplicados, fiz o select de fora usando o distinct no id  da tabela clientes e relacionei as duas tabelas onde "cliente_id" de transacao e "ID" de clientes são iguais 

``` sql

SELECT 
	distinct cliente_id,
    clientes.nome,
    clientes.email,
    clientes.data_cadastro,
    clientes.telefone
FROM transacoes AS t1
inner join
    clientes on t1.cliente_id = clientes.ID
	WHERE t1.id in
        ...
```

Na consulta de dentro nomeei transações como "t2" e relacionei a consulta de fora com a de dentro, 
onde "t1.cliente_id" é igual a "t2.cliente_id" e o ID da consulta de fora é diferente ao ID da consulta de dentro
Isso garante que o ID da transação não será duplicado.

``` sql
		(SELECT
			t1.ID
		FROM
			transacoes t2
		where
			t1.cliente_id = t2.cliente_id and
			t1.ID != t2.ID and 
			DATEDIFF(MINUTE, t1.data, t2.data) < 2 and t2.data < t1.data
		)
```        

Após descobrir os dados dos clientes que tem transações fraudulentas, criei um arquivo 
csv chamado "clientes-fraudulentos.csv" para inserir esses dados, após isso uso a
biblioteca "CSV" para facilitar a importação

Faço a consulta ao banco de dados com a mesma query que usei no SQL Server 

``` py

import csv 

consultando_fraudes = """
SELECT 
	distinct cliente_id, clientes.nome, clientes.email, clientes.data_cadastro, clientes.telefone
FROM transacoes AS t1
inner join clientes
on t1.cliente_id = clientes.ID
	WHERE t1.id in
		(SELECT
			t1.ID
		FROM
			transacoes t2
		where
			t1.cliente_id = t2.cliente_id and
			t1.ID != t2.ID and 
			DATEDIFF(MINUTE, t1.data, t2.data) < 2 and t2.data < t1.data
		)
"""

```

Ultilizo o fetchall() para pegar esses dados e peço para escrever em csv as colunas do arquivo

``` py

cursor.execute(consultando_fraudes)
clientes_fraudulentos = cursor.fetchall()
with open('clientes-fraudulentos.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["id", "nome", "email",
                    "data-cadastro", "telefone"])

``` 

Em seguida faço a iteração usando o for em cada campo do arquivo

```py

for cliente in clientes_fraudulentos:
    print(cliente.cliente_id, cliente.nome, cliente.email, cliente.data_cadastro, cliente.telefone)
    writer.writerow([cliente.cliente_id, cliente.nome, cliente.email, cliente.data_cadastro, cliente.telefone])

```

