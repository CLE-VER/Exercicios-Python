dia = int(input('Coloque o dia do seu nascimento: ')) # o usuário insere o dia em que nasceu

mes = int(input('Coloque o mês em que nasceu: ')) # o mes em que nasceu aqui é lido como 'int', mas pode ser alterado para ler como 'str' também

ano = int(input('coloque o ano em que nasceu: '))

print('você nasceu no dia {}, de {} de {}. certo?'.format(dia,mes,ano)) # mostra os dados que o usuário inseriu no terminal