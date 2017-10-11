a = str(input('Escreva uma palavra'))
b = a[::-1]

if a == b:
    print('Essa palavra é palindrome', a)
else:
    print('Não é palindrome')
