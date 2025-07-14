import os

texto = "Cientista de dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em python.\n"
texto += "E, claro, devem ser profissionais em data science."

arquivo = open(os.path.join(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\cientista.txt"), 'w')


for palavra in texto.split():
    arquivo.write(palavra + ' ')

arquivo.close()

arquivo = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\cientista.txt", 'r')

conteudo = arquivo.read()

arquivo.close()

print(conteudo)

