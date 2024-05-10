from time import sleep
num=int(input('Insira um número aqui: '))
un= num // 1 % 10
dez= num // 10 % 10
cen= num // 100 % 10
mil= num // 1000 % 10
print('Analisando o numero {}'.format(num))
sleep(1)
print('Unidade: {}'.format(un))
sleep(1)
print('Dezena: {}'.format(dez))
sleep(1)
print('Centena: {}'.format(cen))
sleep(1)
print('Milhar: {}'.format(mil))
sleep(1)
