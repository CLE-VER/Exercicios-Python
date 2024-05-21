import math
ang=float(input('digite um ângulo: '))
sen= math.sin(math.radians(ang))
print('O seno de {} é {:.2f}'.format(ang,sen))
cos=math.cos(math.radians(ang))
print('O cosseno de {} é {:.2f}'.format(ang,cos))
tan=math.tan(math.radians(ang))
print('A tangente de {} é {:.2f}'.format(ang,tan))
#-----------
import math

ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno de {} é {:.2f}'.format(ang, sen))
print('O cosseno de {} é {:.2f}'.format(ang, cos))
print('A tangente de {} é {:.2f}'.format(ang, tan))
#-----------
from math import sin, cos, tan
ang=float(input('digite o ângulo aqui: '))
sen=sin(ang)
print('O seno de {} é {:.2f}'.format(ang,sen))
cos=cos(ang)
print('O cosseno de {} é {:.2f}'.format(ang,cos))
tang=tan(ang)
print('A tengente de {} é {:.2f}'.format(ang,tang))