'''020 - SORTEANDO UMA SEQUÊNCIA.
PROGRAMA QUE SORTEI A SEQUÊNCIA ALEATÓRIA DOS NOMES DADOS.'''

from random import shuffle
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
lista = [n1, n2, n3]
shuffle(lista)
print(lista)

import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
lista = [n1, n2, n3]
random.shuffle(lista)
print(lista)
