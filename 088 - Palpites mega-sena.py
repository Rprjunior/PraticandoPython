'''088 - PALPITES MEGA-SENA.
PROGRAMA QUE PERGUNTARÁ QUANTOS JOGOS SERÃO FEITOS E MOSTRARÁ NA TELA UMA SEQUÊNCIA DE PALPITES
DE 6 NÚMEROS ENTRE 1 E 60..'''

from random import randint
from time import sleep

print('-'*35)
print('{:^35}'.format('JOGO MEGA SENA'))
print('-'*35)

lista_jogos = list()
copia_jogos = list()
jogadas = int(input('Quantos jogos serão sorteados? '))
total_jogadas = 1

while total_jogadas <= jogadas:
    contador = 0
    while True:
        numeros_sorteados = randint(1, 60)
        if numeros_sorteados not in lista_jogos:
            lista_jogos.append(numeros_sorteados)
            contador += 1
        if contador >= 6:
            break
    lista_jogos.sort()
    copia_jogos.append(lista_jogos[:])
    lista_jogos.clear()
    total_jogadas += 1

for indice, lista in enumerate(copia_jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)

print('-'*35)
print('{:^35}'.format('>>>>> BOA SORTE <<<<<'))
