maior = 0
menor = 0
for gnt in range(1, 6):
	peso = float(input('Digite o peso da {}° pessoa: '.format(gnt)))
	if gnt == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

