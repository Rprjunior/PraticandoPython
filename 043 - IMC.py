'''043 - IMC.
PROGRAMA QUE PERGUNTE PESO E ALTURA E MOSTRE O IMC
<18.5 - Abaixo do peso
18.5 há 25 - Peso ideal
25 há 30 - Sobrepeso
30 há 40 - Obesidade
40+ - Obesidade Mórbida'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}. Indica:  '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('Peso Ideal.')
elif imc > 25 and imc < 30:
    print('Sobrepeso.')
elif imc > 30 and imc < 35:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')

