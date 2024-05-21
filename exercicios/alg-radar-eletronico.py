vel = float(input('Informe a velocidade em Km que vpcê percorreu: '))
if vel > 80:
	print('Multado por exceder o limite de velocidade de 80Km/h')
	multa = (vel - 80) * 7
	print('Você deve pagar uma mult de {:.2f}'.format(multa))
print( 'tenha um bom dia')
#explicação
'''Se a velocidade for maior que 80, o programa entra no bloco if:
Imprime uma mensagem informando que o usuário foi multado por exceder o limite de velocidade.
Calcula o valor da multa, que é R$7,00 por cada quilômetro por hora acima de 80. Por exemplo, se a velocidade for 90 Km/h, a multa será (90 - 80) * 7 = 70.
Imprime o valor da multa, formatado para mostrar duas casas decimais.'''