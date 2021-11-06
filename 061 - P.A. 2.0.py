'''061 - P.A. 2.0
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA.
Mostre os 10 primeiros termos da progressão usando a estrutura while.'''

valor = int(input('Digite um valor: '))
razao = int(input('Qual será sua razão: '))
contador = 1
while contador <= 10:
    print('{} > '.format(valor), end=' ')
    valor = valor + razao
    contador = contador + 1
print('FIM', end=' ')
