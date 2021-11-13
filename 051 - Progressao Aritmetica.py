'''051 - PROGRESSÃO ARITMÉTICA
'''

valor = int(input('Digite um valor inteiro: '))
razao = int(input('Digite o salto da progressão(razão): '))
print('A partir do VALOR {}, com RAZÃO = {}\nTemos a seguinte Sequência'.format(valor, razao))
for progresso in range(0, 10):
    print('{} > '.format(valor), end=' ')
    valor = valor + razao
print('FIM', end=' ')
