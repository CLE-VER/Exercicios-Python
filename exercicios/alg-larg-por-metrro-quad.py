larg = float(input('largura da parede:'))
alt = float(input('altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área de {}m²'.format(larg,alt,área))
tinta = área / 2
print('Para pintar essa parede, você vai precisar de {:.2f}l de tinta'.format(tinta))
