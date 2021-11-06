'''098 - FUNÇAO CONTADOR
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contador(i, f, s):
    print(f'Contagem de {i} até {f} de {s} em {s}.')
    s = abs(s)
    if s == 0:
        s = 1
    if i > f:
        s = -s
        f = f - 1
    else:
        f = f + 1
    for cont in range(i, f, s):
        print(f'{cont} ', end='')
        sleep(0.5)
    print('FIM')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, -2)
print('Sua vez de personalizar a contagem!')
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
salto = abs(int(input('SALTO: ')))
contador(ini, fim, salto)
