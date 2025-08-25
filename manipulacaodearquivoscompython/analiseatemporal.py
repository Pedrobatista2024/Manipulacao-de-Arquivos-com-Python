import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

df_dsa = pd.read_csv('dadostemporal.csv')

print(df_dsa.shape)

print(df_dsa.head())

print(df_dsa.tail())

#pre_processamento do dados 

#valor monimo da coluna data
print(df_dsa.min())

#valor maximo da coluna data
print(df_dsa.max())

print(df_dsa.info())
#converte a coluna de data no tipo datetime
df_dsa['Data'] = pd.to_datetime(df_dsa['Data'])

print(df_dsa.head())

print(df_dsa.info())

serie_atemporal = df_dsa.set_index('Data')['Total_Vendas']

print(type(serie_atemporal))

print(serie_atemporal)

serie_atemporal = serie_atemporal.asfreq('D')

print(serie_atemporal)