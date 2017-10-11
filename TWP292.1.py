def fatorial(x):
    fat = 1
    for i in range(x):
        fat = fat * x
        x = x - 1
    return fat
