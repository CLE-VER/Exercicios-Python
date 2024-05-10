produto = float(input('informe o valor do produto: R$'))

desc = produto - (produto * 10 / 100)
pgvista = produto - (produto * 15 / 100)
pgparc = produto + (produto * 20 / 100)

print('O produto, se pago à vista, fica por R${:.2f} com o cupom de 15%\ne R${:.2f} com a taxa de 20% da parcela'.format(pgvista,pgparc))

print('O preço do produto com desconto de 10%, equivale a R${:.2f}'.format(desc))

