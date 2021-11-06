'''099 - FUNÇÃO QUE DESCOBRE O MAIOR.
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUEL DELES É O MAIOR.'''

from time import sleep

def maior(* numeros):
    contador = maior = 0
    print('-'*30)
    print('Analisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.5)
        if contador == 0:
            maior = contador
        else:
            if valor > maior:
                maior = valor
        contador = contador + 1
    print(f'\nForam informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#PROGRAMA PRINCIPAL:
maior(5, 4, 8, 9, 2)
maior(3, 5, 2, 7)
maior(3, 2)
maior()
