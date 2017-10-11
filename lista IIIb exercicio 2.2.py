i = 0
notas = [50,20,10,5,2,1]

conta = int(input("Digite o valor da conta: "))
pgto = int(input("Digite o valor Número: "))
troco = pgto - conta

for nota in notas:
    while troco >= nota:
        print("uma nota de", nota)
        troco -= nota
