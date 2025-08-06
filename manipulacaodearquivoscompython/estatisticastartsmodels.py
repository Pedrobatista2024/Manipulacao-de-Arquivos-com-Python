#EXISTE ALGUMA RELAÇÃO ENTRE A AREA DE IMOVEIS
#(EM METROS QUADRADOS) E O VALOR DO ALUGUEL EM
#UMA DETERMINADA CIDADE?? CASO EXISTA RELAÇÃO, 
#PODEMOS MENSURA-LA??

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import statsmodels.api as sm

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

#CONSTRUÇÃO DO MODELO OLS(ORDINARY LEAST SQUARES)
#COM STARTAMODELS EM PYTHON

#print(dados.head())

#definimos a variavel dependente
y = dados['valor_aluguel']

#definimos a variavel independente
x = dados['area_m2']

#o startsmodels requer a adição de uma constante à variável independendte
x = sm.add_constant(x)

#criamos o modelo
modelo = sm.OLS(y, x)

resultado = modelo.fit()

print(resultado.summary())

plt.figure(figsize=(12,8))
plt.xlabel('area_m2', size = 16)
plt.ylabel('valor_aluguel', size= 16)
plt.plot(x['area_m2'], y, 'o', label = 'dados reais')
plt.plot(x['area_m2'], resultado.fittedvalues , label = 'Linha de regressão (previsoes do modelo)')
plt.legend(loc= 'best')
plt.show()