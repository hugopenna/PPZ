dias = int(input('um número de dias'))
horas = int(input('um número de horas'))
minutos = int(input('um número de minutos'))
segundos = int(input('um número de segundos'))

segundos = ((dias * 24 + horas) * 60 + minutos) * 60 + segundos

print (segundos)
