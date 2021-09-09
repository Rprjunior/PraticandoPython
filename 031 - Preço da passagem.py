'''031 - PREÇO DA PASSAGEM.
PROGRAMA QUE LEIA A DISTANCIA DA VIAGEM E MOSTRE O VALOR A SER PAGO DE UM ALUGUEL DE CARRO DE ACORDO COM A QUILOMETRAGEM RODADA.'''

distancia = float(input('Qual a distancia da sua viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
else: preco = distancia * 0.75
print('Sua viagem é de {}km, você pagará {:.2f}R$'.format(distancia, preco))

preco = 0.50 * distancia if distancia <= 200 else distancia * 0.75
print('Sua viagem ficará por {:.2f}R$'.format(preco))

