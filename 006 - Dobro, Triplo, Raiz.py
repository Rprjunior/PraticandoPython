'''006 - OPERAÇÕES MATEMÁTICAS.
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
