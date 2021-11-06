'''065 - REPETINDO VALORES
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 'S'
media = total_numeros = soma = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número inteiro: '))
    soma = soma + numero
    total_numeros = total_numeros + 1
    if total_numeros == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar: [S] ou [N]: ')).upper().strip()[0]
media = soma / total_numeros
print('Foram digitados {} valores, a média entre eles é = {:.2f}'.format(total_numeros, media))
print('O maior valor digitado foi {}, e o menor {}'.format(maior, menor))
print('FIM DO PROGRAMA!')
