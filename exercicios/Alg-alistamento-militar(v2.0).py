from datetime import date

print('Informe o seu gênero: ')
print('''
[1] Masculino
[2] Feminino
''')
op = int(input('Sua opção: '))

if op == 1:
    nasc = int(input('Informe o ano que você nasceu: '))
    atual = date.today().year
    idade = atual - nasc

    print(f'Quem nasceu em {nasc}, tem {idade} anos em {atual}')

    alistamento = ('Seu tempo para se alistar passou! Você já deveria ter se alistado há {} anos.'.format(idade - 18) if idade > 18 else
                   f'Vc tem que se alisar imediatamente' if idade == 18 else 'Ainda faltam {} anos para o alistamento.'.format(
                       18 - idade))
    print(alistamento)
else:
    print('Você não precisa realizar o alistamento obrigatório.')
