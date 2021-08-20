'''012 - DESCONTO DE 5%.
PROGRAMA QUE LEIA O VALOR DE UMA COMPRA E APLIQUE UM DESCONTO DE 5% E MOSTRE NA TELA.'''

Valor = float(input('Qual o valor da peça: '))
NovoValor = Valor - (Valor / 100 * 5)
print('O produto no valor de R${}, com o desconto de 5% ,ficará por R${:.2f}.'.format(Valor, NovoValor))
print ('Total: {:.2f}'.format(Valor - (Valor / 100 * 5)))
