from random import randint
from time import sleep
print('-='*30)
print('{:^60}'.format('JOKENPO'))
print('-='*30)
print('Vamos jogar JOKENPO!\n')
sleep(2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)

print('Suas opções: \n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
jogador = int(input('Sua opção: \n'))
print('Comp jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
if comp == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCER')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVÁLIDA')
elif comp == 1:
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif comp == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
