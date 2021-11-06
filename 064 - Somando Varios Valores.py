'''064 - SOMANDO VÁRIOS VALORES
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

soma = 0
contador = 0
numero = int(input('Escolha um valor - [999 é o comando para PARAR]: '))
while numero != 999:
    contador = contador + 1
    soma = soma + numero
    numero = int(input('Escolha um valor - [999 é o comando para PARAR]: '))
print('A soma dos {} valores digitados é = {}.'.format(contador, soma))
