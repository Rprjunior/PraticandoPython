'''067 - TABUADA 3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

print('--'*20)
print('{:^40}'.format('TABUADA'))
while True:
    print('--'*20)
    numero = int(input('Quer o resultado da tabuada de: '))
    print('--'*20)
    if numero < 0:
        break
    for multiplicar in range(1, 11):
        print('{:2} x {} = {}'.format(multiplicar, numero, multiplicar*numero))
print('Programa encerrado. Volte sempre.')
