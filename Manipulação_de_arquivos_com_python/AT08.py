import csv

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\numeros.csv", 'w') as arquivo:

    #cria objeto de gravação
    write = csv.writer(arquivo)

    #grava no arquivo linha a linha
    write.writerow(('nota1', 'nota2', 'nota3'))
    write.writerow((63,87,92))
    write.writerow((61,79,76))
    write.writerow((72,36,58))

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\numeros.csv", 'r',encoding='utf8', newline='\r\n') as arquivo:

    #cria o objeto de leitura
    leitor = csv.reader(arquivo)

    for x in leitor:
        print(x)

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\numeros.csv", 'r',encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

for linha in dados[1:]:
    print(linha)

