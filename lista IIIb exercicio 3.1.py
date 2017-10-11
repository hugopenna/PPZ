i = 1
div = 0
n = int(input("Número: "))

while i <= n:
    if n % i == 0:
        div += 1
    i += 1

print (div == 2)
