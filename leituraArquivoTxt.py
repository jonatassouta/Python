# NOME DO ARQUIVO
nomeArquivo = 'ArquivoTeste.txt'

# Gerenciando um arquivo texto
# arq = open("<local_arquivo>", "(modo)")
# se o arquivo nao extir, gera um erro

arquivo = open(nomeArquivo, 'r', encoding="utf-8")
# capturando os dados de arquivos
linhas = arquivo.read() # recebe o texto inteiro do arquivo como 1(uma) string
# linhas = arquivo.readlines() #recebe o texto como lista das linhas
# Fechando o arquivo
arquivo.close()


#print(linhas)
#for x in linhas:
 #   print(x)

matriz = linhas.split("\n") # split - transforma em lista segundo uma refelencia 
print(matriz)
###################
print("Fim do Programa.....(gerando arquivo)")

