
import os
from time import sleep
import pandas as pd

import email
import os
from sqlite3 import Cursor
from tkinter import INSERT

from numpy import insert
import pyodbc

print('Listando dados de clientes:\n') 
sleep(2)
pasta = './arquivos-para-analise'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if 'clients-' not in arquivo:
            continue

        caminho = f'{pasta}/{arquivo}'
        df = pd.read_csv(caminho, encoding= 'LATIN-1', sep= ';')
        
        for index, row in df.iterrows():
            # if [0] in row:
            #     print(row[0])
            #     print(f'id = {row[0]}')
            print(f'id = {row[0]}')
            print(f'nome = {row[1]}')
            print(f'email = {row[2]}')
            print(f'data_cadastro = {row[3]}')
            print(f'telefone = {row[4]}')        
            print('')

            dados_de_conexao = (
                "Driver={SQL Server};"
                "Server=BRENO-LAPTOP;"
                "Database=Fraudes;"
            )

            conexao = pyodbc.connect(dados_de_conexao)
            
            cursor = conexao.cursor()
            print('Conexão bem sucedida')

            id_on = "SET IDENTITY_INSERT clientes ON"
            cursor.execute(id_on)
            print('Conexão id on sucedida')

            sqlserver = f"""INSERT INTO clientes(id, nome, email, data_cadastro, telefone) 
                        VALUES('{row[0]}',  '{row[1]}', '{row[2]}', '{row[3].replace(" -0300", "")}', '{row[4]}')"""
            
            

            #PARA EXECUTAR O COMANDO SQL
            print(sqlserver)
            cursor.execute(sqlserver)
            cursor.commit()