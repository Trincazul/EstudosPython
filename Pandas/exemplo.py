import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv', encoding='utf-8', delimiter=';')

#tirando valores 
nrew_df = df.dropna(subset=['Bairro'], inplace = True)
print(df.to_string())

#mostra valores duplicados
print(df.duplicated())

#tira valores duplicados
df.drop_duplicates(inplace = True) 

df['id'].plot()

plt.show()

df.groupby("Bairro").mean()

#mostra os valores unicos
df["Bairro"].unique()

#conta os valores nos dados totais
# tambem pode ser utilizado values_count(normaliza=True)
df["Bairro"].value_counts()

# Preencher todos os valores NaN por um outro específico 
df.fillna(99)
# remoção de quaiquer linhas ou colunas que possuem um np.nan
df.dropna()

#Para ler arquivos CSV codificados em ISO
pd.read_csv('nome_do_arquivo.csv', encoding='ISO-8859-1')

#Para escrever arquivos CSV
pd.to_csv('nome_do_arquivo_para_salvar.csv')

#Removendo colunas utilizando o argumento axis=1
df.drop('País', axis=1)

#Removendo linhas pelo index
s.drop([0, 1]) 

#Quantidade de linhas e colunas do DataFrame
df.shape

#Descrição do Index
df.index 

#Colunas presentes no DataFrame
df.columns 

#Contagem de dados não-nulos
df.count()

#Criando uma nova coluna em um DataFrame:
df['Nova Coluna'] = 0

#Se seu DataFrame possui 3 colunas, passe 3 novos valores em uma lista
df.columns = ['Coluna 1', 'Coluna 2', 'Coluna 3']

#Soma dos valores de um DataFrame
df.sum()

#Menor valor de um DataFrame
df.min()

#Maior valor
df.max()

#Index do menor valor
df.idmin()

#Index do maior valor
df.idmax()

#Resumo estatístico do DataFrame, com quartis, mediana, etc.
df.describe()

#Média dos valores
df.mean()

#Mediana dos valores
df.median()

#Aplicando uma função que substitui a por b
df.apply(lambda x: x.replace('a', 'b'))

#Ordenando em ordem crescente
df.sort_values()

#Ordenando em ordem decrescente
df.sort_values(ascending=False)

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

#Somando todos os valores presentes na Series por 2
s.add(2)

#Subtraindo 2 de todos os valores
s.sub(2)

#Multiplicando todos os valores por 2
s.mul(2)

#Dividindo valores por 2
s.div(2)

#Filtrando o DataFrame para mostrar apenas valores pares
df[df['Bairro'] % 2 == 0]

#Selecionando a primeira linha da coluna nome
df.loc[0, 'Nome']


