horas = int(input("quantas horas você trabalhou esse mês?"))
valor_hora = int(input("quanto você recebe por hora trabalhada?"))

bruto = horas * valor_hora
ir = bruto * 11 / 100
inss = bruto * 8 / 100
sindicato = bruto * 5 / 100
liquido = bruto - ir - inss - sindicato

print ("Seu salário bruto é R$: %d" %bruto)
print ("Seu IR é R$: %.2f" %ir)
print ("Seu INSS é R$: %.2f" %inss)
print ("Sua contribuição do sindicato é R$: %.2f" %sindicato)
print ("Seu salário liquido é R$: %.2f" %liquido)
