minutos = int(input("Quantos minutos você utilizou?"))

if minutos < 200:
    conta = minutos * 0.2
else:
    if minutos > 400:
        conta = minutos * 0.15
    else:
        conta = minutos * 0.18

print ("O valor da sua conta é de R$: ", conta)
