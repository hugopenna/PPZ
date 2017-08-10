v = int(input("qual a velocidade do carro?"))

if v > 110:
    m = (v - 110)*5
    print ("sua multa foi de " , m)

else:
    print ("Parabéns, você está dentro da velocidade permitida")
