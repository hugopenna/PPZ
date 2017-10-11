a = 1
b = 2
c = 3
x = 0

n = int(input("Número: "))

while x < n:
    x = a * b * c
    a,b,c = b,c,c+1

if x == n and x != 0:
    print ("O número %d é triangular de (%d,%d,%d)" %(n,a-1,b-1,c-1))
else:
    print ("O número %d NÃO é triangular" %n)
