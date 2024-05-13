preço = float(input('Informe o preço das compras: R$'))
print('''Escolha a forma de pagamento que deseja efetuar
[1] à vista/cheque
[2] à vista no cartão
[3] parcelar em 2x no cartão
[4] parcelar em 3x ou mais no cartão''')
op = int(input('Sua opção: '))

if op == 1:
    desc = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} alterou para R${:.2f} por conta do desconto de 10%.'.format(preço, desc))
elif op == 2:
    desc = preço - (preço * 5/ 100)
    print('Sua compra no valor de R${:.2f} alterou para R${:.2f} por conta do desconto de 5% aplicado.'.format(preço, desc))
elif op == 3:
    div = preço / 2
    print('Sua compra no valor R${:.2f} ficou por R${:.2f}.'.format(preço, div))
elif op == 4:
    parc = int(input('Em quantas vezes vc quer pagar? '))
    juros = preço + (20 / 100)
    total = juros / parc
    print('Sua compra parcelada em {}x ficou por R${:.2f}'.format(parc, total))
else:
	print('opção inválida, escolha uma das opções de forma de pagamento acima')