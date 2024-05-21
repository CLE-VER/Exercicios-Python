larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt #Cria uma variável que vai armazenar o resultado dos valores da altura e da largura da parede

print('Sua parede tem a dimensão de {} x {} e sua área é de {} m².'.format(larg, alt, area))

tinta = area / 2 # Cria uma variável que vai guardar o resultado da 'area', calculado antrormente, e vai dividir por 2

print('Para pintar essa parede, você vai precisar de {:.2f} l de tinta.'.format(tinta))
