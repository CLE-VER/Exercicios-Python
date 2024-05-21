dist = float(input('Qual a distância em Km que você fará na sua viagem? '))
print('Você irá percorrer uma viagem de {}km'.format(dist))
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(preço))
