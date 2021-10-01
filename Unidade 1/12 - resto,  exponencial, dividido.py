i = 0
numeros = []

while(i<3):
    a = int(input("Digite 3 numeros inteiros: "))
    numeros.insert(i, a)
    i += 1

resto = (numeros[0]) % (numeros[1])
expo = numeros[1]**numeros[2]
div = (numeros[0] / numeros[2]) + numeros[1]
print("O resto do primeiro como segundo é: ", resto)
print("O segundo exponencial com o terceiro: ", expo)
print("O primeiro dividido pelo terceiro, somado com o segundo: ", div)
