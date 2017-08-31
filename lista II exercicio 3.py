kg = 0
excesso = 0
multa = 0
d = 1

while d <=30:
    kg = int(input("hoje é dia %d quantos quilos de peixe você pescou hoje?" %d))
    if kg > 50:
        excesso = kg - 50
        multa = excesso * 4
        print ("Você excedeu em %d, sua multa é de %d" %(excesso, multa))
    else:
        print ("tudo beleza, você não excedeu o limite de hoje.")
    d = d +1

