a = input("Digite uma letra ou numero: ")

a = a.lower()

if a in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print("Você digitou número.")
elif a in ['a', 'e', 'i', 'o', 'u']:
    print("Você digitou uma vogal.")
else:
    print("Digitou uma consoante.")
