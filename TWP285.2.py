meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
dia, mes, ano = input('Digite o ano do seu nascimento (dd/mm/aaa): ').split('/')
print('Nascimento em: %s de %s de %s' %(dia,meses[int(mes)-1],ano))
