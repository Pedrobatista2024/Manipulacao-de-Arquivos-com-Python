with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\cientista.txt",'r') as arquivo:
    texto = arquivo.read()

print(texto)

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\cientista.txt",'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\cientista.txt",'r') as arquivo:
    texto2 = arquivo.read()

print(texto2)