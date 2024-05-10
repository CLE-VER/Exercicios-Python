real = float(input('Quanto você tem em reais? '))

# Substitua 4.96 pelo valor atual da taxa de câmbio do dólar.
taxa_de_cambio = 4.96
dolar = real / taxa_de_cambio

print('Com R${:.2f} você pode obter U${:.2f}'.format(real, dolar))
