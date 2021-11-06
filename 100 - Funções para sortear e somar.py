'''100 - FUNÇÕES PARA SORTEAR E SOMAR
FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR().
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COOCÁ-LOS DENTRO DA LISTA.
A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR'''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores para uma lista: ', end='')
    for contador in range(0, 5):
        numero = randint(1, 10)
        lista.append(numero)
        print(f'{numero} ', end='')
        sleep(0.5)
    print('PRONTO')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores paras entre {lista} temos {soma}.')

numeros = list()
sorteia(numeros)
somaPar(numeros)
