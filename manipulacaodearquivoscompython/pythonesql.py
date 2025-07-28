import sqlite3
import pandas as pd

con = sqlite3.connect('cap12_dsa.db')

cursor = con.cursor()

#sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

#query1 = 'SELECT * FROM tb_vendas_dsa'

#query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

query3 = ''

cursor.execute(query3)

#nomes_colunas = [description[0] for description in cursor.description]

#print(nomes_colunas)

print(cursor.fetchall())

#print(dados)

#print(cursor.fetchall())



