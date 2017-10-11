i= 2
n = int(input("Número: "))
while n > i:
    if n % i == 0:
        print ("O número %d não é primo" %n)
        break
    else:
        i += 1
    print ("O número %d é primo" %n)
