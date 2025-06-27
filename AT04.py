f = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\salarios.csv",'r')

#ler e armazena em forma de string
data = f.read()

#transforma a string em uma lista, dividindo a string pela quebra de linha (\n)
rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

cont = 0
for row in full_data:
    cont += 1

print(cont)