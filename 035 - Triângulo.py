'''035 - TRIÂNGULO.
PROGRAMA QUE LEIA 03 VALORES E MOSTRE SE PODE FORMAR UM TRIÂNGULO.'''

#Crie um programa que diga se as somas dos valores podem formar um triângulo
lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com os valores citados, PODEMOS FORMAR um triângulo.')
else:
    print('Com os valores citados, NÃO PODEMOS FORMAR um triãngulo.')
