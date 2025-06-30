import json
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print('titulo: ',dados['title'])
print('url: ', dados['url'])
print('numero de visualizações: ', dados['stats_number_of_plays'])

arquivo_fonte = r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\dados.json"
arquivo_destino = r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\dados.txt"

with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)


open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())

with open(arquivo_destino,'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)