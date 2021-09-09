'''017 - CATETO E HIPOTENUSA.
PROGRAMA QUE LEIA O COMPRIMENTO DOS CATETOS OPOSTO E ADJASCENTE E MOSTRE A HIPOTENUSA.'''

'''FORMA BÁSICA SEM USAR IMPORTAÇÃO

co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjascente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa é: {:.2f}'.format(hi))
'''

co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjascente: '))
from math import hypot
hi = hypot(co, ca)
print('A hipotenusa é: {:.2f}'.format(hi))

