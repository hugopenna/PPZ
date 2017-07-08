salario = int(input('qual o valor atual do salário'))
aumento = int(input('qual a porcentagem de aumento do salário (0 - 100)'))

aumento = int(salario * aumento / 100)
salario = int(salario + aumento)

print ('aumento' , aumento)
print ('salario' , salario)
