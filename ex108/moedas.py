'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''

from modulomoedas import aumentar, diminuir, metade, dobro, moeda

preco = float(input(f'Qual o valor da compra? R$'))
print(f'Pagando no cartão temos um aumento de 10%, totalizando {moeda(aumentar(preco, 10))}.')
print(f'Pagando à vista temos um desconto de 10%, totalizando {moeda(diminuir(preco, 10))}.')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}.')
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}.')
