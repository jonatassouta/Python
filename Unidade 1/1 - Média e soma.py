# Gerar um programa que calcula a media de n valores,
# ao final mostra a soma, a media, e a quantidade de valores digitados

soma = 0
totalEntrada = 0

while(True):
    entrada = float(input("Entre com um número:"))

    if(entrada == 0):
        break
    
    totalEntrada += 1 #Contador
    soma += entrada #Acumulador

media = soma / totalEntrada
print("A soma é: ", soma)
print("A quantidade de entrada foi: ", totalEntrada)
print("A média é: ", media)