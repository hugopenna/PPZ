i = 0
a = input('Escreva uma palavra: ')
b = ''

while i < len(a):
    if a[i] in 'aeiou':
        b = b + '*'
    else:
        b = b + a[i]
    i += 1
print (b)
