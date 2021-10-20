'''091 - JOGO DE DADOS
PROGRAMA CRIE 04 JOGADORES E OS MESMOS JOGUEM DE FORMA ALEATÓRIA UM DADO
MOSTRE O RANKING PARA SABER QUEM TIROU O MAIOR VALOR'''

from random import randint
from time import sleep
from operator import itemgetter

ranking = list()

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}

print('-'*30)
print(f'{"JOGAR DADOS":^30}')
print('-'*30)

for keys, values in jogo.items():
    print(f'{keys} tirou {values}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-'*20)
print(f'{"RANKING":^20}')
print('-'*20)

for indice, valor in enumerate(ranking):
    print(f'{indice+1}° lugar {valor[0]} com {valor[1]}.')
    sleep(1)

print()
print('FINISH')
