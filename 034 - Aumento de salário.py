'''034 - AUMENTO DE SALÁRIO.
PROGRAMA QUE LEIA UM SALÁRIO E MOSTRE QUANTO FICARÁ O O NOVO SALÁRIO.
15% <= 1500 e 10% > 1500.'''


salario = float(input('Digite seu salário: '))
if salario <= 1500:
    nsalario = salario / 100 * 15 + salario
    print('Seu novo salário terá um aumento de 15% e ficará no valor de: {:.2f}R$'.format(nsalario))
else:
    nsalario = salario / 100 * 10 + salario
    print('Seu novo salário terá um aumento de 10% e ficará no valor de: {:.2f}'.format(nsalario))

