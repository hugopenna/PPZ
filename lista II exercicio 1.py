a = int(input("valor do lado a"))
b = int(input("valor do lado b"))
c = int(input("valor do lado c"))

if a > b + c or b > a + c or c > a + b:
    print ("houston, temos um problema. Isso não é um triangulo")
elif a == b == c:
    print ("seu triangulo é: Equilátero")
elif a == b or b == c or a ==c:
    print ("seu triangulo é: Isósceles")
else:
    print ("seu triangulo é: Escaleno")
