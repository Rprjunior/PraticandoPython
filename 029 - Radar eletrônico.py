'''029 - RADAR ELETRÔNICO.
PROGRAMA QUE LEIA A VELOCIDADE DO CARRO E MOSTRE SE SERÁ MULTADO OU NÃO.'''

velocidade = float(input("Qual a velocidade atual do carro: "))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    print(f'Você pagará uma multa de: {(velocidade - 80) * 7}')
print('Tenha um bom dia! Dirija com atenção.')

