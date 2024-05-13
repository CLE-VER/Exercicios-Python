n1= float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
média = (n1 + n2) / 2

print('A média entre {} e {} é {}'.format(n1, n2, média))
if média >= 7:
	print('aluno aprovado!')
elif média <=5:
    print('aluno em recuperação')
else:
    print('aluno reprovado')
