'''095 - GOLS JOGADOR 2.0
PROGRAMA QUE LEIA UM N0ME DE JOGADOR E QUANTAS PARTIDAS O MESMO JOGOU E QUANTOS GOLS MARCOU EM TODAS AS PARTIDAS.
PODENDO FAZER A PRIMEIRA LEITURA QUANTAS VEZES O USUÁRIO SOLICITAR.
GUARDAR TUDO EM UM DICIONÁRIO E MOSTRAR QUANTOS GOLS MARCOU NO TOTAL.
POR FIM CRIAR UMA FUNÇÃO QUE POSSA CONSULTAR O DESEMPENHO DE CADA JOGADOR INDIVIDUAL.'''

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

    partidas.clear()
    for contador in range(0, total_partidas):
        partidas.append(int(input(f'   - Quantos gols na partida {contador+1}: ')))
    jogador['gols_por_partida'] = partidas[:]
    jogador['total_gols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = input('Quer continuar: [S / N]: ').upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resposta == 'N':
        break

print('cod ', end='')
for indice in jogador.keys():
    print(f'{indice:<20}', end='')
print()

for keys, valor in enumerate(time):
    print(f'{keys:>3} ', end='')
    for dados in valor.values():
        print(f'{str(dados):<20}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe Jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')

        for indice, gol in enumerate(time[busca]['gols_por_partida']):
            print(f'   - No jogo {indice+1} fez {gol} gols.')

print(f'{"VOLTE SEMPRE":^40}')
