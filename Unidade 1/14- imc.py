a = float(input("Qual a sua altura: "))
s = input("Voce é homen ou mulher (m / h)? ")

homen = (72.7 * a) - 58
mulher = (62.1 * a) - 44.7

if(s == "m"):
    print("Seu peso ideal é de : ", mulher)
if(s == "h"):
    print("Seu peso ideal é de : ", homen)