dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos km rodados? '))

pg = dias * 60 + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pg))
