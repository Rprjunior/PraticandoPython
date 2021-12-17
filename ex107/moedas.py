'''107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import modulomoedas

preco = float(input('Qual o valor da compra? R$'))
print(f'Pagando no cartão temos um aumento de 10%, totalizando {modulomoedas.aumentar(preco, 10)}.')
print(f'Pagando à vista temos um desconto de 10%, totalizando {modulomoedas.diminuir(preco, 10)}.')
print(f'O dobro da sua conta seria, {modulomoedas.dobro(preco)}.')
print(f'A metade da sua conta seria, {modulomoedas.metade(preco)}.')
