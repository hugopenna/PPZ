c = int(input("Digite o valor da conta: "))
p = int(input("Digite o valor entregue: "))
t = p - c
n50 = n20 = n10 = 0
n5 = n2 = n1 = 0

while t > 0:
    if t >= 50:
        t -= 50
        n50 += 1
    elif t >= 20:
        t -= 20
        n20 += 1
    elif t >= 10:
        t -= 10
        n10 += 1
    elif t >= 5:
        t -= 5
        n5 += 1
    elif t >= 2:
        t -= 2
        n2 += 1
    else:
        t -= 1
        n1 += 1

print("Troco de ser de %d de 50, %d de 20, %d de 10, %d de 5, %d de 2 e %d de 1" %(n50,n20,n10,n5,n2,n1))
