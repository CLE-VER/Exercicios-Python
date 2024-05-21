acu = 0
sm = 0

for c in range(1, 7):
    num = int(input('Informe um número: '))
    if c % 2 == 0:
        sm += num
        acu += 1
print('Você informou {} números pares e a soma entre eles é: {}'.format(acu, sm))
