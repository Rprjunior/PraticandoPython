'''004 - ANTECESSOR E SUCESSOR
PROGRAMA QUE LEIA UM VALOR E MOSTRE SEU ANTECESSOR E SUCESSOR.'''

n = int(input('Digite uma valor: '))
ant = (n - 1)
suc = (n + 1)
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor {}.'.format(n, ant, suc))
print('O valor é: {}'.format(n))
print('Seu antecessor é: {}'.format(ant))
print('Seu sucessor é: {}'.format(suc))
print('De acordo com o valor {}, seu antecessor é: {}, e seu sucessor: {}'.format(n, (n-1), (n+1)))

