'''063 - FIBONACCI
Escreva um programa que leia um número N inteiro qualquer.
Mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8'''

total = int(input('Digite a quantidade de termos a serem mostrados: '))
termo_1 = 0
termo_2 = 1
contador = 3
print('{} > {}'.format(termo_1, termo_2), end=' ')
while contador <= total:
    termo_3 = termo_1 + termo_2
    print('> {} '.format(termo_3), end=' ')
    termo_1 = termo_2
    termo_2 = termo_3
    contador = contador + 1
