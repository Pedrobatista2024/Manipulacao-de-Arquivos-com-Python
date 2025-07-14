
#abre o arquivo usando with e open, with fecha o arquivo automaticamente.
with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\cientista.txt",'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))

