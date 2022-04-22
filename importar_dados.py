
import os
from time import sleep
import pandas as pd

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