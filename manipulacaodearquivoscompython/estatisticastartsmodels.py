import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm

pd.set_option('display.max_columns', None)

##CARREGANDO OS DADOS

dados = pd.read_csv('dados_casa.csv')

#print(dados.shape)

#print(dados.columns)

#print(dados.head())

#print(dados.info())

##ANALISE EXPLORATORIA

#print(dados.isnull().sum())

#print(dados.describe())

#print(dados['valor_aluguel'].describe())

#print(sns.histplot(data=dados, x='valor_aluguel', kde= True))

#print(dados.corr())
 
#sns.scatterplot(data=dados, x='area_m2', y='valor_aluguel')

##REGRESSÃO LINEAR SIMPLES

#plt.show()
