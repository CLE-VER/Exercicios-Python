from datetime import date

nome = input('Qual o nome do atleta? ')
atual = date.today().year
nasc = int(input('Qual ano de nascimento do atleta: '))
idade = atual - nasc
print('O atleta {} nasceu em {} e tem {} anos'.format(nome, nasc, idade))
if idade <= 9:
	print('CLASSIFICAÇÃO MIRIM')
elif idade <= 14:
	print('CLASSIFICAÇÃO INFANTIL')
elif idade <= 19:
	print('CLASSIFICAÇÃO JUNIOR')
elif idade <= 25:
	print('CLASSIFICAÇÃO SÊNIOR')
else:
	print('CLASSIFICAÇÃO MASTER')
