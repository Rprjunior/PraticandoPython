'''030 - PAR OU ÍMPAR.
PROGRAMA QUE LEIA UM VALOR E MOSTRE SE ELE É PAR OU ÍMPAR.'''

numero = float(input('Digite um valor: '))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')
