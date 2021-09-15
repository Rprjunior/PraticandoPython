'''079 - LISTA, VALORES ÚNICOS.
PROGRAMA QUE PERGUNTE UM VALOR E REPITA QUANTAS VEZES O USUÁRIO QUER ACRESCENTAR UM NOVO VALOR.
CRIE UMA LISTA COM OS VALORES DIGITADOS, NÃO PODENDO CONTER VALORES REPETIDOS.
NO FIM MOSTRE A LISTA EM ORDEM CRESCENTE DOS VALORES.'''

lista = []

while True:
    valores = int(input('Digite um valor: '))
    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não adicionado...')

    resposta = str(input('Quer continuar [S/N]: '))
    if resposta in 'Nn':
        break

lista.sort()
print(f'Os valores digitador foram: {lista}')
