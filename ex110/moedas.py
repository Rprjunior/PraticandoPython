'''Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

from modulomoedas import aumentar, diminuir, metade, dobro, moeda, resumo

preco = float(input(f'Qual o valor da compra? R$'))
resumo(preco, 15, 15)
