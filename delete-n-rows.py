#This is a simple script to delete a given number of rows from a column in a dataset followed by the creation of a new one without the rows

#Libraries 
import pandas as pd
import os
from pandas import read_excel

#Reading the dataset
dfs = pd.read_excel('your-data-set',header=0,engine='openpyxl')
#print(dfs.head)

#Deteing an given number of rows
n = 161
dfn = dfs.drop(dfs[dfs['the-given-column'].eq(1)].sample(n).index)

#Creating the new dataset
writer = pd.ExcelWriter('output-dataset.xlsx')
dfn.to_excel(writer)
writer.save()
print('New dataset created!')
