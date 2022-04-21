import os
pasta = './arquivos-para-analise'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if 'clients' in arquivo:

            print(arquivo)
