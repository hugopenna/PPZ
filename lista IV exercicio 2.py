import random
lista = []
lpar = []
limpar = []
for i in range(20):
    lista.append(random.randint(1,100))
    if lista[i] % 2 == 0:
        lpar.append(lista[i])
    else:
        limpar.append(lista[i])

lista.sort()
lpar.sort()
limpar.sort()

print (lista)
print ('Os números pares são:', lpar)
print ('Os números impares são:',limpar)
