num = int(input('Informe o número que deseja converter: '))
print('''Escolha a base de conversão que vc deseja fazer a conversão:
[1] Conversão binária
[2] Conversão octal
[3] Conversão hexadecimal''')
op = int(input('Escolha uma das opções acima: '))
if op == 1:
	print('O número {} convertido para binário é igual a: {}'.format(num, bin(num)[2:]))
elif op == 2:
	print('O número {} convertido para octal é igual a: {}'.format(num, oct(num)[2:]))
elif op == 3:
	print('O número {} convertido para hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
else:
	print('Ops, tente dnv')
