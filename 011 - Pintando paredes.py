'''011 - PINTANDO PAREDES.
PROGRAMA QUE LEIA LARGURA E ALTURA DE UMA ÁREA E MOSTRE A QUANTIDADE DE TINTA QUE SERÁ NECESSÁRIO
TINTA = 4.5m'''

L = float(input('Qual a Largura da parede: '))
A = float(input('Qual a Altura da parede: '))
AT = L * A
T = AT / 4.5
print('Sua parede tem a dimensão de {} x {}, então sua área é {:.2f}m²'.format(L, A, AT))
print('Para pintar essa área, você precisará de {:.2f}l de tinta'.format(T))

'''015 - ALUGUEL DE CARRO.
PROGRAMA QUE QUANTIDADE DE DIAS, QUILOMETRAGEM RODADA E FAÇA OS CALCULOS PARA DAR O VALOR DO ALUGUEL
DIAS = R$ 60 e KM = R$ 0.15'''

dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input("Quantos Km's foram rodados? "))
Total = (dias * 60) + (km * 0.15)
print('O carro ficou alugado por {} dias, com um total de {:.2f}km rodados, totalizando o pagamento de: R${:.2f}'.format(dias, km, Total))
