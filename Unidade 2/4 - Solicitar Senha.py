nome = input("Digite o nome de usuario: ")
senha = input("Digte uma senha: ")

while (senha == nome):
    print("A senha não pode ser igual ao nome.")
    senha = input("Digite uma nova senha: ")
    
