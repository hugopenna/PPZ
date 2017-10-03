i = 1
a = b = 1
x = int(input("Digite a posição Fibonacci desejada "))
    
while i <= x-2:
    a,b = b,a+b
    i += 1
print ("Fib", b)
