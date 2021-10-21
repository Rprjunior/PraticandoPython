'''094 - UNINDO DICIONÁRIOS E LISTAS
PROGRAMA QUE LEIA NOME, SEXO E IDADE E GUARDE CADA PESSOA EM UM DICIONÁRIO E O DICIONÁRIO NUMA LISTA.
MOSTRE
1 - QUANTAS PESSOAS FORAM CADASTRADAS
2 - A MÉDIA DE IDADE
3 - UMA LISTA COM MULHERES
4 - UMA LISTA COM OS DADOS DE QUEM FICOU ACIMA DA MÉDIA'''

multidao = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M / F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    multidao.append(pessoa.copy())
    while True:
        resposta = input('Quer continuar: [S / N]: ').upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resposta == 'N':
        break

print('-'*30)
print(f'1 - Ao todo temos {len(multidao)} pessoas cadastradas.')

media = soma / len(multidao)
print(f'2 - A média da idade é de {media:4.2f} anos.')

print('3 - As mulheres cadastradas foram: ')
for pessoa in multidao:
    if pessoa['sexo'] in 'Ff':
        print(f'   * {pessoa["nome"]}.')

print('4 - Pessoa(s) acima da média de idade: ')
for pessoa in multidao:
    if pessoa['idade'] >= media:
        print('    ', end=' ')
        for keys, values in pessoa.items():
            print(f'{keys} = {values}', end=' ')
        print()

print('-'*40)
print(f'{"ENCERRADO":^40}')
