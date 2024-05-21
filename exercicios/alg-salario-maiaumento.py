salario = float(input('informe seu salário: R$'))

novo_salario = salario + (salario * 15 / 100) #variável que vai fazer a soma do salario mais os 15% de aumento 

print('Você ganhava R${:.2f} e com o aumento de 15% passa a ganhar R${:.2f}'.format(salario,novo_salario))
