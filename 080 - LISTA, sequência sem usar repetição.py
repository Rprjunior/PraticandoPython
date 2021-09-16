'''080 - LISTA, SEQUÊNCIA SEM USAR REPETIÇÃO.
PROGRAMA QUE PERGUNTE 5 VALORES E GUARDE NUMA LISTA, COLOQUE NA SEQUÊNCIA E MOSTRE NO FINAL'''

lista = []

for contador in range (0, 5):
    valor = int(input('Digite um valor: '))
    if contador == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adicionado a posição {posicao} da LISTA')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram: {lista}')
