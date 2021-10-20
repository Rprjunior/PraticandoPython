'''048 - MULTIPLOS DE 3
PROGRAMA QUE MOSTRE OS MÚLTIPLOS DE 3 DE 0 ATÉ 500 E SOME TODOS OS VALORES'''

soma = 0 #Vamos usar para somar todos os valores.
quantidade = 0 #Vamos usar para saber a quantidade de números usados na operação.
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        print(contador, end=' ')
        soma = soma + contador
        quantidade = quantidade + 1
print('\nA soma dos {} valores é igual a: {}'. format(quantidade, soma))
