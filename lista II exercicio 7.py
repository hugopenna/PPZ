area = int(input("Quantos metros quadrados serão pintados?"))
latas = 0
valor = 0
rendimento_litro = 3
litros_lata = 18
rendimento_lata = rendimento_litro * litros_lata
preco = 80
latas = area / rendimento_lata

if area % rendimento_lata != 0:
    latas = latas + 1
    
valor = latas * preco

print ("você precisará de %d latas de tinta" %latas)
print ("O valor total da sua compra é %d" %valor)
