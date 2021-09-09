'''033 - MAIOR E MENOR.
PROGRAMA QUE LEIA 03 VALORES E MOSTRE QUAL O MAIOR E QUAL O MENOR.'''

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é: {}'.format(menor))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é: {}'.format(maior))

#Outra forma de fazer o código
a1 = int(input('Primeiro valor: '))
b1 = int(input('Segundo valor: '))
c1 = int(input('Terceiro valor: '))
menor1 = a1
if b1 < a1 and b1 < c1:
    menor1 = b1
if c1 < a1 and c1 < b1:
    menor1 = c1
maior1 = a1
if b1 > a1 and b1 > c1:
    maior1 = b1
if c1 > a1 and c1 > b1:
    maior1 = c1
print('O menor valor digitado foi: {}'.format(menor1))
print('O maior valor digitado foi: {}'.format(maior1))

