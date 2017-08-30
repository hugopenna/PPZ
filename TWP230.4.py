n = 1
soma = 0

while n <= 10:
    x = float(input("digite o %d número:" %n))
    soma = soma + x
    n = n + 1

print ("Média: %.2f" %(soma/10))
