a = int(input("Digite um numero entre 0 a 130: "))

while (a < 0 or a > 130):
    a = int(input("Digite um numero entre 0 a 130: "))
    if (a < 0 or a > 130):
        print("Numero invalido!!")