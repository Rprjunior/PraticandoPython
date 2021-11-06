'''055 - MAIOR E MENOR PESO
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maior_peso = 0
menor_peso = 0
for total_peso in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(total_peso)))
    if total_peso == 1:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print('O MAIOR peso descrito foi: {}kg'.format(int(maior_peso)))
print('O MENOR peso descrito foi: {}kg'.format(int(menor_peso)))
