while True:
    nome = str(input("Nome do usuário "))
    senha = str(input("Senha do usuário "))
    if nome == senha:
        print("Nome e senha iguais, digite uma nova senha")
    else:
        print("Cadastro realizado com sucesso")
