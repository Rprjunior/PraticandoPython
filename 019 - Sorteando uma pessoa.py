'''019 - SORTEANDO UMA PESSOA.
PROGRAMA QUE USA A BIBLIOTECA RANDOM PARA SORTEAR AUTOMATICAMENTE UMA PESSOA DAS TRÊS PEDIDAS.'''

from random import choice
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
nomes = [n1, n2, n3]
sortudo = choice(nomes)
print('O sortudo da vez foi {}'.format(sortudo))

import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
nomes = [n1, n2, n3]
sortudo = random.choice(nomes)
print('O sortudo da vez foi {}'.format(sortudo))

