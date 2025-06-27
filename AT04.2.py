#biblioteca para criar arquivo
from setuptools.command.egg_info import write_file

#conteudo do arquivo armazenado em variavel
minhas_linhas = [
    "Olá, esta é a primeira linha",
    "Esta é a segunda linha",
    "E esta é a terceira e última linha."
]

#criando arquivo
write_file(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\salarios2.csv", minhas_linhas,)

arq = open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\salarios2.csv", 'r',encoding="utf-8")

print(arq.read())

arq.seek(0)

print(arq.readline())