nome = ""
idade = 0
salario = 0
cep = 0
dep = ""

def achaTamanho(x):
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)

while (len(nome) <= 3):
    nome = input("Digite o nome do funcionario: ")
    if (len(nome) < 3):
        print("O nome tem que ter pelos menos, 4 caracteres.")

while (idade <= 0 and idade >= 130):
    idade = int(input("Digite a idade do funcionario:  "))
    if (idade <= 0 and idade >= 130):
        print("A idade deve estar entre 0 e 130")

while (salario < 0):
    salario = float(input("Qual o salario: "))
    if (salario < 0):
        print("Deve ser maior que 0.")

while (cep.cout() != 8):
    cep = int(input("Qual o CEP: "))
    if (cep != 8):
        print("Tamnaho do cep deve ser 8.")

while (dep != "Administrativo" or dep != "Fabrica"):
    dep = input("Qual o  departamento: Administrativo ou Fabrica. ")
    if (dep != "Administrativo" or dep != "Fabrica"):
        print("Apenas Administrativo ou Fabrica")
    elif (dep == "Administrativo"):
        a = dep
    elif (dep == "Fabrica"):
        f = dep

print("Nome: ", nome)
print("Idade: ", idade)
print("Salario: ", salario)
print("CEP: ", cep)

if (dep == "Administrativo"):
       print("Departamento: ", a)
elif (dep == "Fabrica"):
        print("Departamento: ", f)
