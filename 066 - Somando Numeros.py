'''066 - SOMANDO NÚMEROS
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

soma = contador = 0
while True:
    valor = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar. [S] ou [N]: ')).upper().strip()[0]
    soma = soma + valor
    contador = contador + 1
    if resposta == 'N':
        break
print(f'Foram digitados {contador} valor(es), a soma é = {soma}.')
