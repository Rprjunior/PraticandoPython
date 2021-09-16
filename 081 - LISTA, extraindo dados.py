'''081 - LISTA, EXTRAINDO DADOS.
PROGRAMA QUE LEIA NÚMEROS DETERMINADOS PELO USUÁRIO E SALVE NUMA LISTA.
MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS DE FORMA DECRESCENTE E SE FOI DIGITADO O VALOR 5.'''

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break

print(f'Vovê digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da LISTA.')
else:
    print('O valor 5 não foi encontrado na LISTA.')