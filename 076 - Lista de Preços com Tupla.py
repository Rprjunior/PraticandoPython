'''076 - LISTA DE PREÇO COM TUPLA.
PROGRAMA QUE POSSUA UMA TUPLA COM PRODUTOS E SEUS VALORES.
MOSTRE A LISTA DE FORMA ORGANIZADA, TABULADA.'''

lista = ('Computador', '2.500',
         'Mouse', '50',
         'Teclado', '80',
         'Fones', '120',
         'Pen Drive', '25',
         'Caixinhas de Som', '75')

print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)
for posicao in range (0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>7}')
