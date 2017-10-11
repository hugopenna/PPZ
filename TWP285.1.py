meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

d = input('Digite o ano do seu nascimento (dd/mm/aaa): ')

d = d.split('/')
mes = meses[int(d[1])-1]

print('Nascimento em: %s de %s de %s' %(d[0],mes,d[2]))
