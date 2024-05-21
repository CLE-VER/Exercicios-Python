real = float(input('Quanto você tem em reais? '))


taxa_de_cambio = 4.96 # cria uma variável que tem o valor do dolar
dolar = real / taxa_de_cambio #cria uma variável que vai armazenar o resultado da dvisão do valor informado pelo usuário  pelo valor da taxa de cambio do dolar

print('Com R${:.2f} você pode obter U${:.2f}'.format(real, dolar))
