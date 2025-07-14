import numpy as np
import os
import matplotlib.pyplot as plt

filename = os.path.join('dadosalunos.csv')

# Supondo que 'dataset.csv' está no mesmo diretório
# O código de leitura das primeiras linhas e o print de arr13 foram omitidos para simplicidade do exemplo

# Carrega as notas de Matemática (coluna 0) e Português (coluna 1)
# var1 será 'Matematica', var2 será 'Portugues'
var1, var2 = np.loadtxt(filename, delimiter = ',', usecols= (0, 1), skiprows= 1, unpack= True)

# Cria o gráfico de dispersão
# 'o' significa que cada ponto será uma bolinha
# markersize = 6 define o tamanho da bolinha
# color = 'red' define a cor da bolinha
plt.plot(var1, var2, 'o', markersize = 6, color = 'red')

# Adiciona rótulos aos eixos para deixar o gráfico claro
plt.xlabel("Nota em Matemática")
plt.ylabel("Nota em Português")
plt.title("Relação entre Notas de Matemática e Português")
plt.grid(True) # Adiciona uma grade para facilitar a leitura

# Exibe o gráfico
plt.show()