'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from modulomoedas import aumentar, diminuir, metade, dobro, moeda

preco = float(input(f'Qual o valor da compra? R$'))
print(f'Pagando no cartão temos um aumento de 10%, totalizando {aumentar(preco, 10, True)}.')
print(f'Pagando à vista temos um desconto de 10%, totalizando {diminuir(preco, 10, True)}.')
print(f'O dobro de {preco} é {dobro(preco, True)}.')
print(f'A metade de {preco} é {metade(preco, True)}.')
