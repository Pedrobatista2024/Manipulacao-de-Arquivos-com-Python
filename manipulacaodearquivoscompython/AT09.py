import json

dict_guido = {'nome': 'guido van rossum',
              'linguagem': 'python',
              'similar':['c','modulo-3', 'lisp'],
              'users': 100000}

for k,v in dict_guido.items():
    print(k,v)

print(json.dumps(dict_guido))

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\dados.json", 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

with open(r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\dados.json", 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados['similar'])

