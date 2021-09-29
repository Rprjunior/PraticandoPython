'''086 - PRIMEIRA MATRIZ.
PROGRAMA QUE CRIE UMA MATRIZ 3x3, LEIA OS VALORES A SEREM PREENCHIDOS
NO FIM MOSTRE A MASTRIZ COM OS VALORES NAS POSIÇÕES CORRETAS.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha}, {coluna}: '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
