salario = float(input('informe seu salário: R$'))

nsalario = salario + (salario * 15 / 100)
print('Você ganhava R${:.2f} e com o aumento de 15% passa a ganhar R${:.2f}'.format(salario,nsalario))
