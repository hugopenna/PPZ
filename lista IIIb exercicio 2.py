i = 0
d = [50,20,10,5,2,1]
n = [0,0,0,0,0,0]

c = int(input("Digite o valor da conta: "))
p = int(input("Digite o valor Número: "))
t = p - c

while t > 0:
    while t >= d[i]:
        n[i] += + 1
        t -= d[i]
    i += 1

print ("Troco de ser de %d de $50, %d de $20, %d de $10, %d de $5, %d de $2 e %d de $1" %(n[0],n[1],n[2],n[3],n[4],n[5]))
