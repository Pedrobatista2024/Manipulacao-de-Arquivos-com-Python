import sqlite3
import pandas as pd

con = sqlite3.connect('cap12_dsa.db')

cursor = con.cursor()

#sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

#query1 = 'SELECT * FROM tb_vendas_dsa'

#query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

#query3 = 'SELECT nome_produto, AVG(unidades_vendidas) FROM tb_vendas_dsa GROUP BY nome_produto'

#query4 = """SELECT nome_produto, AVG(unidades_vendidas)
#            FROM tb_vendas_dsa
#            WHERE valor_unitario > 199
#            GROUP BY nome_produto"""

#query5 = """SELECT nome_produto, AVG(unidades_vendidas)
            #FROM tb_vendas_dsa
            #WHERE valor_unitario > 199
            #GROUP BY nome_produto
            #HAVING AVG(unidades_vendidas) > 10"""

#cursor.execute(query5)

#nomes_colunas = [description[0] for description in cursor.description]

#print(nomes_colunas)

#print(cursor.fetchall())

# APLICANDO SQL COM A SINTAXE DO PYTHON


query = 'SELECT * FROM tb_vendas_dsa'

cursor.execute(query)

dados = cursor.fetchall()

#print(dados)

df = pd.DataFrame(dados, columns= ['id_pedido',
                                   'id_cliente',
                                   'nome_produto',
                                   'valor_unitario',
                                   'unidades_vendidas',
                                   'custo'])

#print(df.head())


#cursor.close()
#con.close()

#media_unidades_vendidas = df['unidades_vendidas'].mean()

#media_unidades_vendidas_por_produto = df.groupby('nome_produto')['unidades_vendidas'].mean()

#media_unidades_vendidas_por_produto = df[df['valor_unitario'] > 199].groupby('nome_produto')['unidades_vendidas'].mean()

#media_unidades_vendidas_por_produto = df[df['valor_unitario'] > 199].groupby('nome_produto')\
#                                            .filter(lambda x: x['unidades_vendidas']\
#                                                    .mean() > 10).groupby('nome_produto')\
#                                                    ['unidades_vendidas'].mean()
#
#print(media_unidades_vendidas_por_produto)






