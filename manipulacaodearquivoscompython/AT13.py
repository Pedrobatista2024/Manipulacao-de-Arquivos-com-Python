import pandas as pd
from pandas import DataFrame

dados = {'Estado':['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano':[2004,2005,2006,2007,2008], 
         'Taxa Desemprego':[1.5,1.7,1.6,2.4,2.7]}

#print(dados)

#df = DataFrame(dados)
#df.head
#print(type(df))

#nova_coluna = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])
df2 = DataFrame(dados,
                columns=['Estado', 'Taxa Desemprego','Taxa de Crescimento', 'Ano'], 
                index=['estado1','estado2', 'estado3', 'estado4', 'estado5'])


print(df2)
