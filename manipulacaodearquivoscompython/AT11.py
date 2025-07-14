import numpy as np
import os
import matplotlib.pyplot as plt

filename = os.path.join('dataset.csv')

try:
    with open(filename, 'r') as f:
        # Imprime as 5 primeiras linhas (ou quantas desejar)
        for i, line in enumerate(f):
            if i < 5: # Altere 5 para o número de linhas que quer ver
                print(line.strip()) # .strip() remove quebras de linha extras
            else:
                break
except FileNotFoundError:
    print(f"Erro: O arquivo '{filename}' não foi encontrado.")

#carregando um dataset para dentro de um array
arr13 = np.loadtxt(filename, delimiter = ',', usecols = (0,1,2,3), skiprows = 1)

print('--' *5)
print(arr13)
print('--' *5)

var1, var2 = np.loadtxt(filename, delimiter = ',', usecols= (0, 1), skiprows= 1, unpack= True)

plt.plot(var1, var2, 'o', markersize = 6, color = 'red') # Primeiro, crie o plot
plt.show() # Segundo, exiba o plot (sem argumentos)