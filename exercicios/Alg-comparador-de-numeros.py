n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
if n1 > n2:
	print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
	print('{} é maior que {}'.format(n2, n1))
else:
	print('Ambos têm o mesmo valor')
	