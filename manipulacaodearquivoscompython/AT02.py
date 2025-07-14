#abre ou cria o arquico para escrita
arquivo2 = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\arquivo2.txt", "w")

#escreve no arquivo
arquivo2.write("aprendendo a programar em python")

#fecha o arquivo
arquivo2.close()

#abre o arquivo para leitura
arquivo2 = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\arquivo2.txt", "r")

#ler o arquivo
print(arquivo2.read())

#abre o arquivo para adicionar alterações
arquivo2 = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\arquivo2.txt", "a")

#altera o arquivo
arquivo2.write(" é a metodologia de ensino da data science academy facilita o aprendizado.")

#fechar o arquivo
arquivo2.close()

#abre o arquivo para leitura
arquivo2 = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\arquivo2.txt", "r")

#ler o arquivo
print(arquivo2.read())

#retorna o cursor para o inicio
arquivo2.seek(0,0)

#ler o arquivo
print(arquivo2.read())