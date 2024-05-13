acu = 0
sm = 0

for c in range(1, 7):
    num = int(input('Informe um número: '))
    if c % 2 == 0:
        sm += num
        acu += 1
print('vc informou {} números e a soma é {}'.format(acu, sm))
