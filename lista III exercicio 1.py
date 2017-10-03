while True:
    x = int(input("Digite um número de 0 a 10 "))
    if x < 0 or x > 10:
        print("Número inválido")
    else:
        print("Número escolhido:", x)
        break
