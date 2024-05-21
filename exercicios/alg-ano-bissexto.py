from datetime import date

ano = int(input(' Qual ano vc irá analisar? '))
if ano == 0:
	ano =  date.today().year #irá pegar o ano atual em que o seu computador está programado
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('O ano {} é bissexto'.format(ano))
else:
	print('O ano {} não é bissexto'.format(ano))