import random

def embaralha(x):
    lista = list(x)
    random.shuffle(lista)
    return ''.join(lista)
