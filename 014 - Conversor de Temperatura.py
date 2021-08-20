'''014 - CONVERSOR DE TEMPERATURA.
PROGRAMA QUE LEIA UMA TEMPERATURA EM CELSIUS E CONVERTA PARA KELVIN E FAHRENHEIT.'''

C = float(input('Digite a temperatura em °C: '))
F = 1.8 * C + 32
K = C + 273
print('De °C{} para °F{}.'.format(C, F))
print('De °C{} para °K{}.'.format(C, K))

