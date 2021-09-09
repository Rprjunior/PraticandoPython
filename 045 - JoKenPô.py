'''045 - JOKENPÔ.
PROGRAMA QUE MOSTRE OPÇÕES DE JOGADA PARA UM JOGADOR E MOSTRE O RESULTADO MÁQUINA PARA SABER QUEM VENCEU.'''

from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
print('{:=^30}'.format('JoKenPô'))
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
print('='*30)
jogador = int(input('Escolha sua jogada: '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('O computador escolheu: {}.'.format(lista[computador]))
print('O jogador escolheu: {}.'.format(lista[jogador]))
if jogador == 0:
    if computador == 0:
        print('\033[33mEMPATE')
    elif computador == 1:
        print('Computador \033[31mVENCEU')
    elif computador == 2:
        print('Jogador \033[32mVENCEU')
elif jogador ==1:
    if computador == 0:
        print('Jogador \033[32mVENCEU')
    elif computador == 1:
        print('\033[33mEMPATE')
    elif computador == 2:
        print('Computador \033[31mVENCEU')
elif jogador == 2:
    if computador == 0:
        print('Computador \033[31mVENCEU')
    elif computador == 1:
        print('Jogador \033[32mVENCEU')
    elif computador == 2:
        print('\033[33mEMPATE')
else:
    print('Opção Inválida. Jogue novamente.')
