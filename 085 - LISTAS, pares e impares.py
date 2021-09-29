'''085 - LISTAS, PARES E IMPARES.
PROGRAMA QUE LEIA SETE VALORES E GUARDE EM UMA ÚNICA LISTA E SEPARE OS PARES DOS ÍMPARES.
NO FIM MOSTRE A LISTA DOS PARES E DOS IMPARES DE FORMA CRESCENTE.'''

lista = [[], []]

for contador in range(1, 11):
    valor = int(input(f'Digite o {contador}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f'Os valores PARES digitados são: {lista[0]}')
print(f'Os valores IMPARES digitados são: {lista[1]}')
