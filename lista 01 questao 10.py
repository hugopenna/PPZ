fumante_anos = int(input('Há quantos anos você fuma?'))
cigarros_dia = float(input('quantos cigarros por dia você fuma?'))

total_cigarros = int(fumante_anos * 365 * cigarros_dia)
tempo = int((total_cigarros * 10) / (24 * 60))

print (total_cigarros)
print (tempo)
