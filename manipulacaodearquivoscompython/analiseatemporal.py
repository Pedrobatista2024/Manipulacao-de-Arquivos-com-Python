import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df_dsa = pd.read_csv('dadostemporal.csv')

#print(df_dsa.shape)
#
#print(df_dsa.head())
#
#print(df_dsa.tail())
#
##pre_processamento do dados 
#
##valor monimo da coluna data
#print(df_dsa.min())
#
##valor maximo da coluna data
#print(df_dsa.max())
#
#print(df_dsa.info())
##converte a coluna de data no tipo datetime
df_dsa['Data'] = pd.to_datetime(df_dsa['Data'])

#print(df_dsa.head())
#
#print(df_dsa.info())

serie_atemporal = df_dsa.set_index('Data')['Total_Vendas']

#print(type(serie_atemporal))
#
#print(serie_atemporal)
#
serie_atemporal = serie_atemporal.asfreq('D')

#print(serie_atemporal)

#grafico serie temporal(sem formatação)
#plt.figure(figsize=(12,6))
#plt.plot(serie_atemporal)
#plt.xlabel('Data')
#plt.ylabel('Venda')
#plt.title('Serie Temporal de vendas')
#plt.grid(True)
#plt.show()

#grafico serie temporal(comm formatação)

#cria o grafico da serie temporal com layout de constraste
#plt.figure(figsize=(12,6))
#plt.plot(serie_atemporal, color= 'white', linewidth=2)
#
##cores e estilos
#plt.gca().set_facecolor('#2e03a3')
#plt.grid(color='yellow', linestyle='--',linewidth=0.5)
#
##rotulos titulos e legenda
#plt.xlabel('Data', color= 'black', fontsize=14)
#plt.ylabel('Venda', color= 'black', fontsize=14)
#plt.title('Serie Temporal de vendas', color= 'black', fontsize=18)
#
##cores dos eixos e dos ticks(marcadores)
#plt.tick_params(axis= 'x', colors= 'black')
#plt.tick_params(axis= 'y', colors= 'black')
#
#plt.show()

#analise e previsão de serie temporal com suavização exponencial

#cria modelo
modelo = SimpleExpSmoothing(serie_atemporal)

#treinamento (ajuste) do modelo
modelo_ajustado = modelo.fit(smoothing_level=0.2)

#extrai os valores previstos pelo modelo
suavizacao_exponencial = modelo_ajustado.fittedvalues

#plot
#plt.figure(figsize=(12,6))
#plt.plot(serie_atemporal, label= 'Valores Reais')
#plt.plot(suavizacao_exponencial, label= 'Valores Previstos', linestyle= '--')
#plt.xlabel('Data')
#plt.ylabel('Vendas')
#plt.title('Modelo de Suavização Exponencial')
#plt.show()

#fazer previsões
num_previsoes = 1
previsoes = modelo_ajustado.forecast(steps= num_previsoes)

print('Previsão do Total de Vendas para Janeiro/2024', round(previsoes[0], 4))
