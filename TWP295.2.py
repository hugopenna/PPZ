import random

def embaralha(x):
    a = ''
    lista = list(x)
    random.shuffle(lista)
    for i in lista:
        a = a + i

    print (a)
