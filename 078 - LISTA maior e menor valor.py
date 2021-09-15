'''078 - LISTA MAIOR E MENOR VALOR.
PROGRAMA QUE LEIA 5 VALORES E GUARDE EM UMA LISTA.
MOSTRE QUAL O MAIOR E MENOR VALOR E SUAS RESPECTIVAS POSIÇÕES.'''

lista = []
maior = menor = 0

for contador in range (0, 5):
    lista.append(int(input('Digite um valor: ')))
    if contador == 0:
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        if lista[contador] < menor:
            menor = lista[contador]

print(f'Os valores digitados foram: {lista}')

print(f'O MAIOR valor digitado foi {maior}, na posição: ', end=' ')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'O MENOR valor digitado foi {menor}, na posição: ', end=' ')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}...', end='')
