import csv
import sqlite3

conn = sqlite3.connect('sqldb.db')

conn.execute('''CREATE TABLE producao (
                produto TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                receita_total REAL
             )''')

conn.commit()
conn.close()

with open('producao_alimentos.csv', 'r') as file:
    reader = csv.reader(file)

    next(reader)

    conn = sqlite3.connect('sqldb.db')

    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?,?,?,?)', row)

    conn.commit()
    conn.close()

print('Job Concluido Com Sucesso¹')