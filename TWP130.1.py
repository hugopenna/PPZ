minutos = int(input("Quantos minutos você utilizou?"))

if minutos < 200:
    conta = minutos * 0.2
elif minutos <= 400:
    conta = minutos * 0.18
elif minutos <= 800:
    conta = minutos * 0.15
else:
    conta = minutos * 0.08

print ("O valor da sua conta é de R$: ", conta)
