preco = int(input('qual o preço da mercadoria'))
desconto = int(input('qual a porcentagem de desconto (0 - 100)'))

desconto = int(preco * desconto / 100)
preco = int(preco - desconto)

print ('desconto' , desconto)
print ('preço' , preco)
