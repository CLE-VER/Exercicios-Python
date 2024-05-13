

#----------
while True:
    try:
        num = int(input('Informe o número que deseja converter (ou digite -1 para sair): '))
        if num == -1:
            break
        print('''\nEscolha a base de conversão:
[1] Conversão binária
[2] Conversão octal
[3] Conversão hexadecimal''')
        opcao = int(input('Escolha uma das opções acima: '))
        if opcao == 1:
            resultado = bin(num)[2:]
            print(f'O número {num} convertido para binário é igual a: {resultado}')
        elif opcao == 2:
            resultado = oct(num)[2:]
            print(f'O número {num} convertido para octal é igual a: {resultado}')
        elif opcao == 3:
            resultado = hex(num)[2:]
            print(f'O número {num} convertido para hexadecimal é igual a: {resultado}')
        else:
            print('Ops, opção inválida. Tente novamente.')
    except ValueError:
        print('Por favor, insira um número inteiro válido.')

