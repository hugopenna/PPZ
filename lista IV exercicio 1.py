import random
lista = []
for i in range(10):
    lista.append(random.randint(1,100))
lista.sort()

print (lista)
print ('O menor número é: ', lista[0])
print ('O maior número é: ', lista[-1])
