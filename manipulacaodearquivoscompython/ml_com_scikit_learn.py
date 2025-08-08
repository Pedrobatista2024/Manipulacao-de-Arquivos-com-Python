#USANDO DADOS HISTORICOS É POSSIVEL PREVER O SALARIO DE
#ALGUEM COM BASE NO TEMPO DEDICADO AOS ESTUDOS EM HORAS
#POR MÊS??

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dados = pd.read_csv(r'C:\Users\estudante\Desktop\Pedro\GitHub\ManipulacaoArquivos\manipulacaodearquivoscompython\dados_ml.csv')

#print(dados.shape)

#print(dados.columns)

#print(dados.head())

#print(dados.info())

#print(dados.isnull().sum())
#
#print(dados.corr())
#
#print(dados.describe())
#
#print(dados['horas_estudo_mes'].describe())

#sns.histplot(data= dados, x= 'horas_estudo_mes', kde= True)
#plt.show()

# x precisa ser uma matrix
x = np.array(dados['horas_estudo_mes'])
#corrigindo o shape
x = x.reshape(-1, 1)

y = dados['salario']

#plt.scatter(x, y, color= 'Blue', label= 'dados reais historicos')
#plt.xlabel('Horas de estudos')
#plt.ylabel('Salario')
#plt.legend()
#plt.show()

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

print(x_treino.shape)

print(x_teste.shape)

print(y_treino.shape)

print(y_teste.shape)