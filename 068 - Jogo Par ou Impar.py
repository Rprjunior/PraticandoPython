'''068 - JOGO PAROU ÍMPAR
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder.
Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

vitorias = 0
from random import randint
print('=-='*10)
print('{:^30}'.format('JOGO DO PAR OU ÍMPAR'))
while True:
    print('=-=' * 10)
    jogador = int(input('Escolha um valor de 0 a 10: '))
    computador = randint(0, 10)
    total = jogador + computador
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Impar - [P] ou [I]: ')).upper().strip()[0]
        print('=-='*10)
    print(f'Jogador jogou {jogador}\nComputador jogou {computador}\nSoma = \033[33m{total}\033[m')
    print('Resultado deu PAR.' if total % 2 == 0 else 'Resultado deu ÍMPAR.')
    if par_impar in 'P':
        if total % 2 == 0:
            print('Você \033[32mVENCEU\033[m!')
            vitorias = vitorias + 1
        else:
            print('Você \033[31mPERDEU\033[m!')
            print('=-='*10)
            break
    elif par_impar in 'I':
        if total % 2 == 1:
            print('Você \033[32mVENCEU\033[m!')
            vitorias = vitorias + 1
        else:
            print('Você \033[31mPERDEU\033[m!')
            print('=-='*10)
            break
    print('Vamos jogar novamente.')
print(f'GAME OVER. Você ganhou {vitorias} vezes.')
