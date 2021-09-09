'''038 - COMPARANDO NÚMEROS,
PROGRAMA QUE PERGUNTE DOIS VALORES E MOSTRE QUAL DELES É O MAIOR.'''

#Programa que leia dois valores e diga qual é maior ou se são iguais.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
if numero1 > numero2:
    print('{} é MAIOR que {}. Então o primeiro número é maior.'.format(numero1, numero2))
elif numero1 < numero2:
    print('{} é MENOR que {}. Então o segundo número é maior'.format(numero1,numero2))
else:
    print('{} e {} são IGUAIS.'.format(numero1, numero2))

