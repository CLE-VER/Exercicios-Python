num = int(input(' insira aqui um número e irei verificar se ele é Par ou Impar'))
result = num % 2
if result == 0:
	print(' o numero {} é PAR'.format(num))
else:
	print(' o numero {} é IMPAR'.format(num))