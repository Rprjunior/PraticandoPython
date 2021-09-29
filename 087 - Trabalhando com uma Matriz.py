'''087 - TRABALHANDO COM UMA MATRIZ.
PROGRAMA QUE CRIE UMA MATRIZ 3x3, LEIA OS VALORES A SEREM PREENCHIDOS
MOSTRE A MASTRIZ COM OS VALORES NAS POSIÇÕES CORRETAS. NO FIM MOSTRE
1 - A SOMA DE TODOS OS VALORES PARES DIGITADOS
2 - A SOMA DOS VALORES DA TERCEIRA COLUNA
3 - O MAIOR VALOR DA SEGUNDA LINHA'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_coluna = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição {linha}, {coluna}: '))

for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print(f'A soma dos valores PARES é igual {soma_pares}.')

for linha in range(0, 3):
    soma_terceira_coluna += matriz[linha][2]
print(f'A soma dos valores da TERCEIRA COLUNA é igual {soma_terceira_coluna}.')

for contador in range(0, 3):
    if contador == 0:
        maior_segunda_coluna = matriz[1][contador]
    elif matriz[1][contador] > maior_segunda_coluna:
        maior_segunda_coluna = matriz[1][contador]
print(f'O MAIOR valor da segunda LINHA é {maior_segunda_coluna}.')
