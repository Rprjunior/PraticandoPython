'''037 - CONVERSOS DE BASES NUMÉRICAS.
PROGRAMA QUE PERGUNTE UM VALOR E TRANSFORME EM BASE NÚMERA DE ACORDO COM A SOLICITADA.'''

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print('{} CONVERTIDO para BINÁRIO é igual a: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} CONVERTIDO para OCTAL é igual a: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} CONVERTIDO para HEXADECIMAL é igual a: {}'.format(numro, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')

