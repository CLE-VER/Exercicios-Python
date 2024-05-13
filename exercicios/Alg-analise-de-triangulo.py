s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo semento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
	print('Os segmentos podem formar um triângulo')
	if s1 == s2 == s3:
		print('Equilátero')
	elif s1!= s2 != s3 != s1:
		print('Escalêno')
	else:
		print('Isosceles')
else:
	print('Os segmentos não podem formar um triângulo')
	