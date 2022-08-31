
import os
from time import sleep
import pandas as pd

import os

from numpy import insert
import pyodbc

dados_de_conexao = (
    "Driver={SQL Server};"
    "Server=BRENO-LAPTOP;"
    "Database=Fraudes;"
)

conexao = pyodbc.connect(dados_de_conexao)
            
cursor = conexao.cursor()

id_on = "SET IDENTITY_INSERT clientes ON"
cursor.execute(id_on)

print('Listando dados de clientes:\n') 
sleep(2)
pasta = './arquivos-para-analise'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if 'clients-' in arquivo:
            caminho_clientes = f'{pasta}/{arquivo}'
            df = pd.read_csv(caminho_clientes, encoding= 'LATIN-1', sep= ';')
            
            for index, row in df.iterrows():
                consulta_id = f"select 1 from clientes where id = '{row[0]}'"
                cursor.execute(consulta_id)
                resultado = cursor.fetchone()

                if resultado is not None and resultado[0] == 1:
                    print(f'Ignorando cliente {row[1]}')
                    continue

                
                clientes = f"""INSERT INTO clientes(id, nome, email, data_cadastro, telefone) 
                            VALUES('{row[0]}',  '{row[1]}', '{row[2]}', '{row[3].replace(" -0300", "")}', '{row[4]}')"""
                            
                cursor.execute(clientes)
                cursor.commit()
                print(f'cliente id = {row[0]}, inserido com sucesso')

print('\n')
print('Listando arquivos de transações:\n') 
sleep(2)
pasta = './arquivos-para-analise'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if "transaction-" in arquivo:
            caminho_transacoes = f'{pasta}/{arquivo}'
            df = pd.read_csv(caminho_transacoes, encoding= 'LATIN-1', sep= ';')                    
            for index, row in df.iterrows():
                consulta_id = f"select 1 from clientes where id = '{row[1]}'"
                cursor.execute(consulta_id)
                existe_cliente = cursor.fetchone()
                if not existe_cliente:
                    print(f'Ignorando id de transacoes {row[0]}')
                    continue

                consulta_transacao = f"select 1 from transacoes where id = '{row[0]}'"
                cursor.execute(consulta_transacao)
                transacao_ja_cadastrada = cursor.fetchone()
                
                if transacao_ja_cadastrada:
                    print(f'Ignorando transacoes {row[0]}')
                    continue

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
                