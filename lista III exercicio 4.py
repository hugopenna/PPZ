i = 2
f = [1,1]
a = b = 1
x = int(input("Digite a posição Fibonacci desejada "))
    
while i < x:
    a,b = b,a+b
    f.append(b)
    i += 1
print (f[x-1])
