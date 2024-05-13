soma = 0
acu = 0
val = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        acu = acu + 1
    val = val + 1
print('Existem {} números divisiveis por 3 entre 1 e 500. A soma entre os {} valores solicitados é {} '.format(val, acu, soma))
