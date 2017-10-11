import random

def embaralha(x):
    i = 0
    a = ''
    lista = list(x)
    random.shuffle(lista)
    while i < list.__len__(lista):
        a = a + lista[i]
        i = i + 1

    print (lista)
    print (a)
