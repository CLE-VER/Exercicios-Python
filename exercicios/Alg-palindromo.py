coisa = str(input('Digite alguma coisa: ')).strip().upper()
palavra = coisa.split()
junt = ''.join(palavra)
inv = ''
for letra in range(len(junt) -1, -1, -1):
	inv += junt [letra]
print(' o inverso de {} é {}'.format(junt, inv))
if inv == junt:
	print('é um palindromo')
else:
	print('não é um palindromo')
	
#-----------

coisa = str(input('Digite alguma coisa: ')).strip().upper()
palavra = coisa.split()
junt = ''.join(palavra)
inv = junt [::-1]

print(' o inverso de {} é {}'.format(junt, inv))
if inv == junt:
	print('é um palindromo')
else:
	print('não é um palindromo')