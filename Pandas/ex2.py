# Estruturas de dados do pandas
import pandas as pd

# Criando um pseries
pseries = pd.Series([7,13, np.nan,21,33])
print(pseries)

# Criando um Dataframe
dt = [1, 2, 3, 7] # Lista de dados
df1 = pd.Dataframe(dt)
df1

# Carregando arquivo CSV
dados.pd.read_csv('arquivo.csv')

# Gravando em um arquivo CSV
dados.pd.read_csv('arquivo.csv')

# Gravando em um arquivo Excel
dados.to_excel('novosdados.xlsx', sheet_name = 'Sheet1')

# Crianco arquivo CSV a partir de dataframe
dados.to_csv("dados.csv")

# O .head() demonstra as 5 primeiras linhas do DataFrame
df_market.head()

# é usado para visualizar alguns resultados estatísticos como percentil, média, padrão, etc.
df_market.describe()

# Aplicando describe() por coluna
df_market["Rating"].describe()

# .info() função Pandas é usada para obter um resumo conciso do dataframe.df_market.info()
df_market.info()

# retornar o formato do dataframe, primeiro termo quantidade de linhas e segundo total de colunas.
 df_market.shape
# (1000, 17)
 
# Ordenação baseando-se em coluna - ordem crescente na coluna Total
df_market.sort_values("Total") 

# Visualização por colunas selecionadas
df_market['City'].sort_values(ascending=False)

# Criação de subsets do DataFrame
#----------------------------------

cols_dados = ["City", "Quantity", "Unit price", "Date"]
df_market[cols_dados]

# Em "Product line" filtrar por "Electronic accessories"
df_market[df_market["Product line"] == "Electronic accessories"]

# Aplicando mais de uma condição
df_market_yangon_eletacc = df_market[(df_market["City"] == "Yangon") & (df_market["Product line"] == "Electronic accessories")]
df_market_yangon_eletacc.head() 

# Criando uma nova coluna e aplicando uma operação matemática entre as variáveis
df_market["Ticket"] = df_market["Total"] / df_market["Quantity"]
df_market 

#  Agregando os dados
# -------------------------------------------------------------------

# Média dos valores
df_market["Total"].mean()

# Valor mínimo
df_market["Total"].min()

# Valor máximo
df_market["Total"].max()

# Retorna valores no quantil* fornecido sobre o eixo solicitado
df_market.quantile(0.25)

# Valor moda - representa o valor mais frequente de um conjunto de dados
df_market["Quantity"].mode()

# Usada para obter um resumo conciso do dataframe - suas variáveis e tipos dos dados
df_market.info()

# Criando acúmulo .describe é um exemplo desse tipo, e gera vários dados estatísticos:
df_market.describe()

# Método .agg — Agregue usando uma ou mais operações
# Para uma função ou lista de funções a serem aplicadas em uma série
# ou mesmo em cada elemento da série separadamente.

df_market["Rating"].agg([np.mean, max, min])


# Excluindo duplicidade  categoricos Payment Número de identificação da fatura do recibo de venda gerado por computador
df_market_id = df_market.drop_duplicates(subset="Payment")
df_market_id #não observado valores duplicados

# Contagem de valores

df_market["Product line"].value_counts()

# A porcentagem dos dados por gênero
df_market[[ "Gender"]].value_counts(normalize=True)


# Agrupamento — Groupby
#--------------------------------------------------------------------

# Agrupamento por "City" com a média de "Unit price"
df_market.groupby("Product line")["Unit price"].mean().sort_values(ascending = False)

# Agrupamento com mais de uma variável
df_market.groupby("Product line")[["Unit price", "Total"]].mean().sort_values("Total", ascending = False)

# Agrupamento com multiplas estatísticas
df_market.groupby("Product line")[["Quantity", "Total"]].agg([min, max,sum])


# Tabelas Dinâmicas

# O objeto gerado é um frame — estrutura de dados tabular bidimensional, mutável
# em tamanho e potencialmente heterogênea, com eixos rotulados (linhas e colunas).

# Utilizando pivot_table
t2 = df_market.pivot_table(values="Quantity", index="Product line")
t2

# Fatiar e indexar

# São diversas as possibilidades de selecionar um subconjunto de dados ou elementos individuais
# sendo o índice uma escolha.

# As colunas do dataset
df_market.columns

df_market.index

# Configurar uma coluna como índice
df_market_ind = df_market.set_index("Invoice ID")
df_market_ind.head(3)

# Removendo índice
df_market_id.reset_index()

# Multinível para índice
df_market_id3 = df_market.set_index(["Branch", "City"])

df_market_id3.loc[["C", "B"]]

# Slicing com colunas
df_market.loc[:, "City":"Product line"]

# Slicing por posição
df_market2.iloc[2:10, 1:5]

#--------------------------------------------------------------------

# Valores ausentes — (missing)

# Os dados ausentes são comuns em conjuntos e análises de dados, 
# eles são excluídos nos métodos e objetos de estatística descritiva — devido a ausência de dados.
# No Pandas é utilizado o valor de ponto flutuante NaN (Not a Number) para representá-los.
# Há disponível diversos métodos, aqui vamos utilizar alguns deles.

# Criando uma lista por coluna
lista = {
"nome": ["João", "Maria", "Caio", "Jose"],
"sexo": ["H", "F", "M", "F"],
"produto": ["limão", "mamão", "laranja", "maça"],
"peso_kg": ["1.2", "2,5", "3.5", np.nan],
"valor_total": [10.48, 22.5, 14.4, np.nan]
}

# Criando um novo dataframe
df2 = pd.DataFrame(lista)
df2


# Total de valores ausentes por coluna
df2.isna().sum()


# Plotando valores ausentes
df2.isna().sum().plot(kind="bar")
plt.show()


# Removendo valores missing
df2.dropna()


# Preenchendo valores ausentes, no caso abaixo com 0:
df2.fillna(0)

