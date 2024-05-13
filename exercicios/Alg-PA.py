pri = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = pri + (10 - 1) * razão  # para achar o décimo termo de uma razão
for c in range(pri, décimo + razão, razão):
    print('{}'.format(c), end='-> ')