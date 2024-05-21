n = str(input('digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
# explicação: O método .split() divide a string n em uma lista de palavras, usando espaços como separador padrão. Cada palavra se torna um elemento da lista nome.
'''print('Seu primeiro nome é {}'.format(nome[0])): Esta linha imprime o primeiro elemento da lista nome, que é o primeiro nome do usuário.
print('Seu último nome é {}'.format(nome[len(nome)-1])): Esta linha imprime o último elemento da lista nome. len(nome) retorna o número de elementos na lista, e len(nome)-1 é o índice do último elemento'''