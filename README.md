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
