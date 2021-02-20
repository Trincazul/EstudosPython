import pandas as pd 

pd.read.csv('dados.csv', sep = ';').head()
df = pd.read_csv('dados.csv', sep = ';')
df.dtypes