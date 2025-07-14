from os.path import split

f = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\salarios.csv",'r')

#ler e armazena em forma de string
data = f.read()

#transforma a string em uma lista, dividindo a string pela quebra de linha (\n)
rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print((full_data))

