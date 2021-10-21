'''093 - GOLS JOGADOR DE FUTEBOL
PROGRAMA QUE LEIA UM N0ME DE JOGADOR E QUANTAS PARTIDAS O MESMO JOGOU E QUANTOS GOLS MARCOU EM TODAS AS PARTIDAS
GUARDAR TUDO EM UM DICIONÁRIO E MOSTRAR QUANTOS GOLS MARCOU NO TOTAL.'''

jogador = dict()
partidas = list()

jogador['nome'] = input('Nome do jogador: ')
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for contador in range(0, total_partidas):
    partidas.append(int(input(f'   - Quantos gols na partida {contador+1}: ')))
jogador['gols_por_partida'] = partidas[:]
jogador['total_gols'] = sum(partidas)

print('-'*60)
print(jogador)
print('-'*60)

for keys, values in jogador.items():
    print(f'O campo {keys} tem valor {values}.')

print('-'*40)
print(f'O jogador {jogador["nome"]} jogou {total_partidas} partidas.')
for indice, valor in enumerate(jogador["gols_por_partida"]):
    print(f'   - Na partida {indice+1}, fez {valor} gols.')
print(f'Totalizando {jogador["total_gols"]} gols.')