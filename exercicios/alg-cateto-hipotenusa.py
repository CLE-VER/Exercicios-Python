catop = float(input('Qual o comprimento do cateto oposto? '))
catad = float(input('Qual o comprimento do cateto adjacente? '))
hip = (catop**2 + catad**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
#----------
import math

catop = float(input('Qual o comprimento do cateto oposto? '))
catad = float(input('Qual o comprimento do cateto adjacente? '))
hip = math.sqrt(catop**2 + catad**2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
