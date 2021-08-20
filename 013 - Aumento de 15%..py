'''013 - AUMENTO 15%.
PROGRAMA QUE LEIA UM VALOR E APLIQUE A SOMA DE 15% E MOSTRE O RESULTADO.'''

Sal = float(input('Qual o seu salário: R$ '))
NSal = Sal + (Sal / 100 * 15)
print('O salário era R$ {:.2f}, e passa a ser R$ {:.2f}.'.format(Sal, NSal))
print('Novo Salário = R$ {:.2f}'.format(Sal + (Sal / 100 * 15)))

