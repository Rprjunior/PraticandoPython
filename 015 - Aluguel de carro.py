'''015 - ALUGUEL DE CARRO.
PROGRAMA QUE QUANTIDADE DE DIAS, QUILOMETRAGEM RODADA E FAÇA OS CALCULOS PARA DAR O VALOR DO ALUGUEL
DIAS = R$ 60 e KM = R$ 0.15'''

dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input("Quantos Km's foram rodados? "))
Total = (dias * 60) + (km * 0.15)
print('O carro ficou alugado por {} dias, com um total de {:.2f}km rodados, totalizando o pagamento de: R${:.2f}'.format(dias, km, Total))
