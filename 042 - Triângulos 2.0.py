'''042 - TRIÂNGULOS 2.0.
PROGRAMA QUE PERGUNTE 03 VALORES E MOSTRE SE PODE FORMAR UM TRIÂNGUO E QUAL É.'''

l1 = float(input('Digite o primeiro valor: '))
l2 = float(input('Digite o segundo valor: '))
l3 = float(input('Digite o terceiro valor: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com os valores citados PODEMOS formar um triângulo: ', end='')
    if l1 == l2 and l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('ESCALENO')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('ISÓSCELES')
else:
    print('Com os valores citados NÃO PODEMOR formar um triângulo.')

