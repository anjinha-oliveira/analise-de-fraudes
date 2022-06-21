import os 
import pandas as pd



pasta = './arquivos-para-analise'
for diretorio, sbpastas, arquivos in os.walk(pasta):
    for arquivo in sorted(arquivos):
        if "transaction-" in arquivo:
            print(arquivo)