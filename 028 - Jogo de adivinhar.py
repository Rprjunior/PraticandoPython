'''028 - JOGO DE ADIVINHAR.
PROGRAMA QUE LEIA UM VALOR ENTRE 1 E 5 E MOSTRE SE FOI O MESMO QUE A MÁQUINA ESCOLHEU.'''

from random import randint
computador = randint(1, 5)
print('-=-'*20)
print('De 1 a 5, tente adivinhar em que número pensei...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei: '))
if jogador == computador:
    print('PARABÉNS, você venceu!')
else:
    print(f'A poderosa máquina venceu. Eu pensei no número {computador} e não no número {jogador}!')

