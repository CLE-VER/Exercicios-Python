
frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {}x '.format(frase.count('A'))) # Conta e mostra o número de vezes que a letra 'A' apareceu na frase



print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))# Encontra e mostra a posição da primeira letra 'A' na frase


print('A última letra "A" aparece na posição {}'.format(frase.rfind('A')+1)) # Encontra e mostra a posição da última letra 'A' na frase
