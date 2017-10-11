import random

def inteiros(x):
    lista = []
    k = 0
    while k < x:
        a = random.randint(10,100)
        lista.append(a)
        k = k + 1
    print (lista)
