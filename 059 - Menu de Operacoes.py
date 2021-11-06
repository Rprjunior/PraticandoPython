'''059 - MENU DE OPERAÇÕES
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
opcao = 0
maior_numero = 0
while opcao != 5:
    opcao = int(input('''Escolha o que fazer entre os números:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MOSTRA O MAIOR
    [4] ESCOLHER NOVOS VALORES
    [5] ENCERRAR
    Escolha uma opção: '''))
    print('-==-'*10)
    if opcao == 1:
        print('A soma entre {} + {} é = {}'.format(numero1, numero2, (numero1+numero2)))
    elif opcao == 2:
        print('A Multiplicação entre {} * {} é = {}'.format(numero1, numero2, (numero1*numero2)))
    elif opcao == 3:
        if numero1 > numero2:
            maior_numero = numero1
        elif numero1 < numero2:
            maior_numero = numero2
        print('O maior numero entre {} e {} é = {}'.format(numero1, numero2, maior_numero))
    elif opcao == 4:
        numero1 = int(input('Digite o 1° valor novo: '))
        numero2 = int(input('Digite o 2° valor novo: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-==-'*10)
    sleep(2)
print('Fim do programa!')
