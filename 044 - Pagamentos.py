'''044 - PAGAMENTOS.
PROGRAMA QUE PERGUNTE O VALOR DA OMPRA A FORMA DE PAGAMENTO E MOSTRE COMO FICARÁ PAGANO A VISTA OU CARTÕES.'''

print('{:=^40}'.format('LOJAS DANJU'))
valor = float(input('Qual o valor da compra: '))
print('{:=^40}'.format('OPÇÕES DE PAGAMENTO'))
print('''[1] À vista
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print('=' * 40)
pagamento = int(input('Qual a opção de pagamento: '))
if pagamento == 1:
    total = valor - (valor / 100 * 10)
    print('Total da compra = {}R$, com o desconto ficará por {:.2f}R$.'.format(valor, total))
elif pagamento == 2:
    total = valor - (valor / 100 * 5)
    print('Total da compra = {}R$, com o desconto ficará por {:.2f}R$.'.format(valor, total))
elif pagamento == 3:
    total = valor
    parcela = valor / 2
    print('Sua compra no valor de R${:.2f}, ficará em 2x de R${:.2f}'.format(total, parcela))
elif pagamento == 4:
    total = valor + (valor / 100 * 20)
    parcela = int(input('Em quantas parcelas será dividido: '))
    parcelas = total / parcela
    print('Sua compra no valor de R${:.2f}, ficará {}x de R${:.2f}'.format(valor, parcela, parcelas))
else:
    print('Opção Inválida. Tente Novamente.')

