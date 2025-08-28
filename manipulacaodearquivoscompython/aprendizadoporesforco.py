import random
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('acoes.csv')

#print(df.shape)
#
#print(df.head())

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open= df['AAPL.Open'],
                high= df['AAPL.High'],
                low= df['AAPL.Low'],
                close= df['AAPL.Close'])])

fig.show()

precos = df['AAPL.Close'].values

print(type(precos))

#import random
#import plotly.graph_objects as go
#import pandas as pd
#import numpy as np
#from datetime import datetime
#
#df = pd.read_csv('acoes.csv')
#
#fig = go.Figure(data=[go.Candlestick(x=df['Date'],
#                                     open= df['AAPL.Open'],
#                                     high= df['AAPL.High'],
#                                     low= df['AAPL.Low'],
#                                     close= df['AAPL.Close'])])
#
## A nova linha de código para salvar o gráfico como um arquivo HTML
#fig.write_html('grafico_acoes.html')
#
#precos = df['AAPL.Close'].values
#print(type(precos))

print('\nDefinindo os Hiperparâmetros de Q-Learning...')
nun_episodios = 1000
alfa = 0.1
gama = 0.99
epsilon = 0.1

print('\nConfigurando o Ambiente de Negociação...')
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

def executar_acao(estado, acao, saldo, num_acoes, preco):
    #ação comprar
    if acao == 0:
        if saldo >= preco:
            num_acoes += 1
            saldo -= preco
    #acção de vender
    elif acao == 1:
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco
    #define o lucro
    lucro = saldo + num_acoes * preco - saldo_inicial

    return (saldo, num_acoes, lucro)

#inicializar a tabela Q
print('\nInicializar a tabela Q')
q_tabela = np.zeros((len(precos), len(acoes)))

#treinamento
print('\nInicializando o treinamento...')
for _ in range(nun_episodios):
    #define o saldo
    saldo = saldo_inicial

    #define o numero de ações
    num_acoes = num_acoes_inicial

    for i, preco in enumerate(precos[:-1]):
        estado = i

        #escolher a ação usando a politica epsilon-greedy
        if np.random.random() < epsilon:
            acao = random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])

        #executar a ação e obter a recompensa e o proximo estado
        saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i + 1

        #atualizar a tabela Q
        q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])

print('\nTreinamento concluido')

#valores iniciais para tstar o agente 
saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('\nExecutando o agente...')
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)

print('\nExecução Concluida')

print(num_acoes)

precos[-1]

#vendedo todas as ações no ultimo preço
saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro, 2)

print(f'Começamos com de 1000 e tivemos {lucro_final} de lucro')