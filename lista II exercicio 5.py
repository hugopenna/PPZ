a = int(input("digite o num a"))
b = int(input("digite o num b"))
c = int(input("digite o num c"))

while a < b or b < c:
    if c > b:
        b,c = c,b
    elif b > a:
        a,b = b,a

print (a,c)
