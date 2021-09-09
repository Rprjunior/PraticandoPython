'''010 - CONVERSOR DE DÓLAR.
PROGRAMA QUE LEIA UM VALOR E FAÇA A COTAÇÃO EM DÓLAR.'''

R = float(input('Digite um valor R$: '))
D = R / 5.06
print('Esse valor R${}, convertido para US$ fica: US${:.1f}'.format(R,D))
print('Você tem R${}, se trocar por US$ ficará: US${:.2f}'.format(R, (R/5.06)))
