a = int(input("Digite o número A "))
b = int(input("Digite o número B "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print ("O MDC entre A e B é %d" %a)
