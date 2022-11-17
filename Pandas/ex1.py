import pandas as pd

# Data Frame vazio
df = pd.DataFrame(columns = ['Ano', 'Valor_vendas', 'Qtde_itens', 'Mes'])

# ### Adicionando linhas com o Append
df = df.append({'Ano': 2011, 'Valor_vendas': 135000, 'Qtde_itens': 270, 'Mes': 'Jan'}, ignore_index = True)

# criando uma lista [] de dicionários {}
dados_vendas_anuais = [{'Ano': 2011, 'Valor_vendas': 119000, 'Qtde_itens': 430, 'Mes': 'Fev'},
                      {'Ano': 2011, 'Valor_vendas': 185000, 'Qtde_itens': 520, 'Mes': 'Mar'},
                      {'Ano': 2011, 'Valor_vendas': 198000, 'Qtde_itens': 550, 'Mes': 'Abr'},
                      {'Ano': 2011, 'Valor_vendas': 204000, 'Qtde_itens': 560, 'Mes': 'Mai'},
                      {'Ano': 2012, 'Valor_vendas': 235000, 'Qtde_itens': 600, 'Mes': 'Jan'},
                      {'Ano': 2012, 'Valor_vendas': 254000, 'Qtde_itens': 620, 'Mes': 'Fev'},
                      {'Ano': 2012, 'Valor_vendas': 244000, 'Qtde_itens': 605, 'Mes': 'Mar'},
                      {'Ano': 2012, 'Valor_vendas': 260000, 'Qtde_itens': 640, 'Mes': 'Abr'},
                      {'Ano': 2012, 'Valor_vendas': 268000, 'Qtde_itens': 649, 'Mes': 'Mai'}]

# exemplo de como abrir um arquivo e renomear as colunas
# adicionar header=1 para omitir o cabeçalho anterior
df1 = pd.read_csv('df_1.csv', names=['Ano', 'Valor_vendas', 'Qtde_itens', 'Mes'], header=1)


# inserindo várias linhas através da lista e do append
df = df.append(dados_vendas_anuais, ignore_index= False) # False vai começar um novo index nas linhas inseridas

# inserindo várias linhas através da lista e do append
df = df.append(dados_vendas_anuais, ignore_index= True) # True vai ignorar o index novo e dar sequência ao index do DataFrame

#### Adicionando linhas com o loc
df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']

# inserindo uma nova linha com o .loc
df.loc['t'] = [2012, 273000, 657, 'Jun']

# ### Alterando linhas com o iloc
df.iloc[19]

# inserindo uma nova linha com o iloc
df.iloc[19] = [2012, 278000, 667, 'Jun']

# ### Agrupando dados
# agrupando por ano 
df.groupby(['Ano']).head()

# agrupando por ano e somando os valores
df.groupby(['Ano']).sum()

# agrupando por ano e contando os valores
df.groupby(['Ano']).count()

# filtrando colunas e agrupando por ano e somando os valores
df[['Ano', 'Valor_vendas', 'Qtde_itens']].groupby(['Ano']).sum()

# Filtrando, agrupando e somando os valores 
df[['Mes', 'Valor_vendas', 'Qtde_itens']].groupby(['Mes']).sum()

#### Tratando duplicados
df.duplicated()
df.drop_duplicates()
df.sort_values(['Ano', 'Mes'])
df.drop_duplicates(inplace=True)

# inserindo uma linha com o append
df = df.append({'Ano': 2011, 'Valor_vendas': 135000, 'Qtde_itens': 270, 'Mes': 'Jan'}, ignore_index = True)
df = df.drop_duplicates()
df.drop_duplicates(inplace=True)
