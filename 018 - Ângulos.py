'''018 - ÂNGULOS.
PROGRAMA QUE LEIA UM ÂNGULO E MOSTRE SEU SENO / COSSENO E TANGENTE.'''

from math import radians, cos, sin, tan
ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
print ('O ângulo de {:.0f} tem o SENO de {:.2f}.'.format(ang, seno))
cosseno = cos(radians(ang))
print ('O ângulo de {:.0f} tem o COSSENO de {:.2f}.'.format(ang, cosseno))
tangente = tan(radians(ang))
print ('O ângulo de {:.0f} tem a TANGENTE de {:.2f}.'.format(ang, tangente))

