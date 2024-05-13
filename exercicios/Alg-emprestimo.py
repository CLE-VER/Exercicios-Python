casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos ano você irá pagar a casa? '))
prestação = casa / (anos * 12)
mínimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
	print('Emprestimo \033[32m CONCEDIDO!\033[m')
else: 
	print('Emprestimo \033[31m NEGADO!\033[m')
