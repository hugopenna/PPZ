import random

lista = []
k = 0
while len(lista) < 15:
    a = random.randint(10,100)
    if a not in lista:
        lista.append(a)
lista.sort()
print (lista)
