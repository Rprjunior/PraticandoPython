'''006 - OPERAÇÕE MATEMÁTICAS.
PROGRAMA QUE LEIA UM VALOR E MOSTRE SEU DOBRO / TRIPLO / RAIZ / RAIZ CÚBICA.'''

n1 = int(input('Digite um valor: '))
print('O dobro de {} é: {}.\n '
    'O triplo de {} é: {}.\n A raíz quadrade de {} é: {:.2f}.\n '
    'A raíz cubíca de {} é: {:.2f}'.format(n1, (n1*2), n1, (n1*3), n1, (n1**(1/2)), n1, (n1**(1/3))))
n = int(input('Digite um valor: '))
d = (n * 2)
t = (n * 3)
r = (n**(1/2))
rc = (n ** (1/3))
print('O dobro de {} é: {}'.format(n, d))
print('O triplo de {} é: {}'.format(n, t))
print('A raíz de {} é: {:.2f}'.format(n, r))
print('A raiz cúbica de {} é: {:.2f}'.format(n, rc))

'''010 - CONVERSOR DE DÓLAR.
PROGRAMA QUE LEIA UM VALOR E FAÇA A COTAÇÃO EM DÓLAR.'''


R = float(input('Digite um valor R$: '))
D = R / 5.06
print('Esse valor R${}, convertido para US$ fica: US${:.1f}'.format(R,D))
print('Você tem R${}, se trocar por US$ ficará: US${:.2f}'.format(R, (R/5.06)))
