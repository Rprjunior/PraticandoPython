'''PROGRAMA QUE LEIA O NOME E VALOR DE UM PRODUTO, PERGUNTE SE QUER CADASTRAR MAIS E POR FIM MOSTRE:
[1] TOTAL DA COMPRA [2] PRODUTOS COM CUSTO MAIOR QUE 1 MIL [3] PRODUTO MAIS BARATO'''

print('='*40)
print('{:^40}'.format('LOJA DIGITAL'))

totalcompra = maiormil = maisbarato = contador = 0
produtobarato = ' '

while True:
    print('='*40)
    produto = str(input('Nome do produto? '))
    valor = float(input('Valor do produto R$ '))
    totalcompra += valor
    contador += 1

    if valor > 1000:
        maiormil += 1
    if contador == 1:
        maisbarato = valor
        produtobarato = produto

    else:
        if valor < maisbarato:
            maisbarato = valor
            produtobarato = produto
    resposta = ' '

    while resposta not in 'SN':
        resposta = str(input('Quer continuar: [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

print('='*40)
print('{:^40}'.format('FIM DO PROGRAMA'))
print('='*40)

print(f'O total da compra foi de {totalcompra}')
print(f'Foram registrados {maiormil} produtos com valor acima de 1 mil R$.')
print(f'O produto mais barato foi {produtobarato} que custou {maisbarato}')
