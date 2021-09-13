'''074 - ANÁLISE DE DADOS EM TUPLA.
PROGRAMA QUE LEIA 4 VALORES E GUARDE NUMA TUPLA.
1 - QUANTAS VEZES APARECEU O VALOR 09.
2 - EM QUAL POSIÇÃO APARECEU O PRIMEIRO VALOR 03.
3 - QUAIS FORAM OS NÚMEROS PARES.'''

numeros = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(f'Os valores digitados foram: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição: {numeros.index(3)+1}°')
else:
    print('Não foi digitado nenhum valor 3')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
