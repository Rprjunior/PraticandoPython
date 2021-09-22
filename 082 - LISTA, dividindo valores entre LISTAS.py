'''082 - LISTA, DIVIDINDO VALORES ENTRE LISTAS.
PROGRAMA QUE LEIA VÁRIOS VALORES E GUARDE NUMA LISTA.
DIVIDA OS VALORES IMPARES E PARES EM OUTRAS DUAAS LISTAS E MOSTRE AS 3 NO FINAL.'''

numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break

for indice, valor in enumerate(numeros):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)

print(f'A LISTA completa é: {numeros}')
print(f'A LISTA de PARES é: {pares}')
print(f'A LISTA de ÍMPARES é: {impares}')
