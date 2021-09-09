'''007 - MÉDIA ARITMÉTICA.
PROGRAMA QUE LEIA 3 VALORES E MOSTRE A MÉDIA ENTRE ELES.'''

nome = (input('Digite seu nome: '))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
m = ((n1 + n2 + n3) / 3)
print('Sua média {}, é: {:.2f}'.format(nome, m))
print('Sua média {}, somadas entre:\n 1° Nota - {}\n 2° Nota - {}\n'
    ' 3° Nota - {}\n Média: {:.2f}'.format(nome, n1, n2, n3, (n1+n2+n3)/3))
