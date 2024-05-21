from time import sleep # importando a biblioteca time

import emoji # importando a biblioteca emoji

print('lançamento T menos  . . .')
for c in range(10, 0, -1):  # contagem regressiva
    print(c)
    sleep(1)
print(emoji.emojize('lançamento bem sucedido '':dashing_away:'' :rocket:',language='alias'))