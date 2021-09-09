'''023 - DIVISOR DE NÚMEROS.
PROGRAMA QUE LEIA UM VALOR E MOSTRE ALGUMAS VARIAÇÕES.'''

numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Analisando o número {numero}.\nTemos em UNIDADE: {unidade}.\nTemos em DEZENA: {dezena}.\nTemos em CENTENA: {centena}\nTemos em MILHAR: {milhar}')
print(f'Analisando o número {numero}.')
print(f'Temos em UNIDADE: {unidade}.')
print(f'Temos em DEZENA: {dezena}.')
print(f'Temos em CENTENA: {centena}.')
print(f'Temos em MILHAR: {milhar}.')
