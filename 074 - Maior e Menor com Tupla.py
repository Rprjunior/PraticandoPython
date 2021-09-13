'''074 - MAIOR E MENOR COM TUPLA.
PROGRAMA QUE MOSTRE 05 VALORES QUE TEM NA TUPLA DE FORMA ALEATÓRIA E DIGA QUAL O MENOR E O MAIOR.'''

from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores gerados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO MAIOR valor gerado foi: {max(numeros)}')
print(f'O MENOR valor gerado foi: {min(numeros)}')
