import pandas as pd
import numpy as np
from pandas import DataFrame
import sklearn
from sklearn.datasets import load_iris


#dados = {'Estado':['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         #'Ano':[2004,2005,2006,2007,2008], 
         #'Taxa Desemprego':[1.5,1.7,1.6,2.4,2.7]}

#print(dados)

#df = DataFrame(dados)
#df.head
#print(type(df))

#nova_coluna = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])
#df2 = DataFrame(dados,
               # columns=['Estado', 'Taxa Desemprego','Taxa de Crescimento', 'Ano'], 
               # index=['estado1','estado2', 'estado3', 'estado4', 'estado5'])

#df2['Taxa de Crescimento'] = np.arange(5.)

#fatiamento de dataframes do pandas
#print(df2.dtypes)

#print(df2['estado2': 'estado4'])

#print(df2[df2['Taxa Desemprego'] < 2])

#print(df2[['Estado', 'Taxa de Crescimento', 'Ano']])

dsa_df = pd.read_csv('manipulacaodearquivoscompython/datasetpd.csv')

#print(dsa_df.head())

#print(dsa_df.isna().sum())

moda = dsa_df['Quantidade'].value_counts().index[0]

#print(moda)
dsa_df.loc[:, 'Quantidade'] = dsa_df['Quantidade'].fillna(value=moda)

#print(dsa_df.isna().sum())
#print(dsa_df.Valor_Venda.describe())



df2 = dsa_df.query('229 < Valor_Venda < 10000')

#print(df2.Valor_Venda.describe())

df3 = df2.query('Valor_Venda > 766')

dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]

#print(df3.head())

#print(dsa_df.shape)

#print(dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])])

#print(dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])].shape)

#print(dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10])

#print(dsa_df[(dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South')].head(5))

#print(dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail)

#print(dsa_df[(dsa_df.Segmento != 'Home Office') | (dsa_df.Regiao != 'South')].sample(5))

#agrupamento

#print(dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())

#print(dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))

#manipulação de strings

#print(dsa_df[dsa_df.Segmento.str.startswith('Con')].head())

#print(dsa_df[dsa_df.Segmento.str.endswith('umer')].head())

#split de strings em dataframe do pandas

#print(dsa_df['ID_Pedido'].head)

#print(dsa_df['ID_Pedido'].str.split('-'))

#print(dsa_df['ID_Pedido'].str.split('-').str[1].head())

#dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]

#strip de strings em dataframes no pandas

#print(dsa_df['Data_Pedido'].str.lstrip('20', inpl))

#Substituir strings

#print(dsa_df.head())

#dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')

#Combinar strings

dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep= '-')

#Construção de graficos com pandas
#print(dsa_df.head()) 

data = load_iris()

df = pd.DataFrame(data['data'], columns= data['feature_names'])
df['species'] = data['target']
#print(df.head())

#print(df.plot())

#print(df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)'))

columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)','sepal width (cm)']
#print(df[columns].plot.area())

#print(df.groupby('species').mean().plot.bar())

#print(df.groupby('species').count().plot.pie(y= 'sepal width (cm)'))

#print(df[columns].plot.box(figsize = (8,8)))

#FIM