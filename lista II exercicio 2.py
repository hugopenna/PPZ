a = int(input("digite o ano"))

if a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
    print ("esse ano é bisexto")
elif a % 4 == 0 and a % 100 == 0:
    print ("esse ano NÃO é bisexto")
elif a % 4 == 0:
    print ("esse ano é bisexto")
else:
    print ("esse ano NÃO é bisexto")
