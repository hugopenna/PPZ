n = 0
x = int(input("Número: "))

while n * (n +1) * (n + 2) < x:
    n += 1
    
print ((n * (n + 1) * (n + 2)) == x)
