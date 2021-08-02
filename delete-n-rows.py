#Thiago Nishimura de Sousa(SP3040364) e Gabriel Afonso de Brito(Sp3015106)
#Este script tem como objetivo excluir n linhas da coluna evolucao, tendo como condicao o valor 1

#Bibliotecas utilizadas
import pandas as pd
import os
from pandas import read_excel

#Lendo o arquivo
dfs = pd.read_excel('your-data-set',header=0,engine='openpyxl')
#print(dfs.head)

#Excluindo n quantidade de linhas de acordo com a condição
n = 161
dfn = dfs.drop(dfs[dfs['evolucao'].eq(1)].sample(n).index)

#Escrevendo uma nova planilha com dfn
writer = pd.ExcelWriter('output-planilhav6.xlsx')
dfn.to_excel(writer)
writer.save()
print('Nova plhanilha criada!')
