# NOME DO ARQUIVO
nomeArquivo = 'ArquivoTeste.txt'

# Gerenciando um arquivo texto
# arq = open("<local_arquivo>", "(modo)")
# modo = w Se não existir cria, se exisir ele substitui
# modo = a Se não existir cria, se exisir ele acrecenta

arquivo = open(nomeArquivo, 'a', encoding="utf-8")


#arquivo.write("Testo3\n")

for x in range(4, 11):
    arquivo.write("Testo" + str(x) + "\n")

# Fechando o arquivo
arquivo.close()

###################
print("Fim do Programa.....(gerando arquivo)")