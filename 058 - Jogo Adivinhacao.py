'''058 - JOGO ADIVINHAÇÃO
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar
Mostre no final quantos palpites foram necessários para vencer.'''

from random import randint
chance = 1
computador = randint(1, 10)
jogador = int(input('''Acabei de pensar em um número entre 1 e 10.
Será que você consegue adivinhar qual foi?
Qual o seu palíte? '''))
while not computador == jogador:
    if jogador < computador:
        jogador = int(input('''Mais... Tente novamente.\nQual o seu palpite? '''))
    if jogador > computador:
        jogador = int(input('''Menos... Tente novamente.\nQual o seu palpite? '''))
    chance = chance + 1
if chance == 1:
    print('Parabéns, você é bom, acertou de primeira')
elif 2 <= chance <= 5:
    print('Você precisou de \033[32m{}\033[m chances. Precisa treinar mais para me vencer!'.format(chance))
else:
    print('Foram \033[31m{}\033[m chances. Estar muito longe de me vencer. HAHAHAHAHA!'.format(chance))
