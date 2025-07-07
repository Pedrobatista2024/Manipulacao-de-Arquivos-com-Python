#abrindo o aqrquivo para leitura
arquivo1 = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\arquivo1.txt", "r")

#lendo o arquivo
print(arquivo1.read())

#contar o numero de caracteres
print(arquivo1.tell())

#retornar o cursor para o inicio do arquivo
print(arquivo1.seek(0,0))

#ler um numero exato de caracteres
print(arquivo1.read(23))