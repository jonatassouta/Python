

a = int(input("Digite 3 numeros inteiros-> A "))
b = int(input("Digite 3 numeros inteiros-> B "))
c = int(input("Digite 3 numeros inteiros-> C "))

if (a > b and a > c):
    print(a ,"A É O MAIOR")
elif(b > a and b > c):
    print(b ,"B É O MAIOR")
else:
    print(c , "C É O MAIOR")