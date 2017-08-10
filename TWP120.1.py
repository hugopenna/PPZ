minutos = int(input("Quantos minutos você utilizou?"))

if minutos < 200:
    conta = minutos * 0.2
else:
    if minutos <= 400:
        conta = minutos * 0.18
    else:
        if minutos <= 800:
            conta = minutos * 0.18
        else:
            conta = minutos * 0.08

print ("O valor da sua conta é de R$: ", conta)
