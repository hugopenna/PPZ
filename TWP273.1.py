i = 0
notas = []
soma = 0
while i < 4:
    n = float(input("Insira a nota"))
    notas.append(n)
    i += 1
    soma += n

print ("Notas:", notas)
print ("Média %4.2f" %(soma/4))
