import pandas as pd

#muda as configurações para o pandas exibir todas as colunas
pd.set_option('display.max_columns', None)

#variavel com o caminho do arquivo
arquivo = r"C:\Users\estudante\Desktop\Pedro\Cursos\AnalisePython\arquivos\salarios.csv"

#ler o arquivo e armazena na variavel
df = pd.read_csv(arquivo)

#ler as primeiras 20 linhas do arquivo
print(df.head(20))

#conta qunatos resgistro tem para cada valor na coluna position tittle
print(df['Position Title'].value_counts())