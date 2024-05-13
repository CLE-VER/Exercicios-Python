num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0: #número primo só é divisível por 1, 2 e por ele mesmo
        print('\033[34m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('por isso ele não é primo')
