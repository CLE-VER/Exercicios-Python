from datetime import date
	
atual = date.today().year

nasc = int(input('Informe o ano que vc nasceu: '))
idade = atual - nasc

print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
	print('Você tem que se alistar imediatamente')
elif idade < 18:
	saldo = 18 - idade
	print('Ainda faltam {} anos para o alistamento.'.format(saldo))
	ano = atual + saldo
	print('Seu alistamento irá acontecer em {}.'.format(ano))
elif idade > 18:
	saldo = idade - 18
	print('vc já deveria ter se alistado há {} anos.'.format(saldo))
	ano = atual - saldo
	print('Seu alistamento foi em {}.'.format(ano))