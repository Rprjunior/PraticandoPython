'''053 - POLÍDROMOS
'''

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = ''
for sequencia in range(len(juntar) -1, -1, -1): #len = ultima posição até a possição -1 porque a ultima não conta e contagem regressiva.
    inverso = inverso + juntar[sequencia]
print('O inverso de {} é {}.'.format(juntar, inverso))
if inverso == juntar:
    print('A sequência é um PALÍNDRMOMO.')
else:
    print('A sequência não é um PALÍNDROMO.')
