from setuptools.command.egg_info import write_file

f = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\salarios.csv",'r')

#ler e armazena em forma de string
data = f.read()

#transforma a string em uma lista, dividindo a string pela quebra de linha (\n)
rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

#pega a primeira coluna
first_row = full_data[0]
cont = 0

#conta as colunas da primeira linha
for column in first_row:
    cont += 1

print(cont)

