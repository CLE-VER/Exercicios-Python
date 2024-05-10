from random import randint, choice
from time import sleep
lista = [0,5]
print('Tente adivinhar um número que eu estou pensando.')
sleep (2)
print('Se acertar eu pouparia a vida da Terra.')
sleep(2)
print('caso contrário . . .' 
      'MUAHAHAHA')
num = int(input('Tenta a sorte e adivinhe um número de 0 a 5: '))
print('Hmm. . .')
sleep(3)
escolhido = choice(lista)
print('Desta vez vc venceu' if num == escolhido else 'tenta mais uma vez, eu deixo')
