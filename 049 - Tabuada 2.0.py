'''049 - TABUADA 2.0
CRIE UM PROGRAMA QUE LEIA UM VALOR E MOSTRE A TABUADA ATÉ 10'''

numero = int(input('Quer o resultado da tabuada de: '))
for multiplicar in range(1, 11):
    print('{:2} x {} = {}'.format(multiplicar, numero, multiplicar*numero))
