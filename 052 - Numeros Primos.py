'''052 - NÚMEROS PRIMOS
'''

numero = int(input('Digite um valor: '))
totaldivisoes = 0
for sequencia in range(1, numero + 1):
    if numero % sequencia == 0:
        print('\033[32m', end=' ')
        totaldivisoes = totaldivisoes + 1
    else:
        print('\033[31m', end=' ')
    print(sequencia, end=' ')
print('\nO número {} foi divido {} vezes.'.format(numero, totaldivisoes))
if totaldivisoes == 2:
    print('\n\033[mPor isso é número PRIMO')
else:
    print('\n\033[mPor isso NÃO é número PRIMO')
