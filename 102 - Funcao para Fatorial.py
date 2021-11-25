'''102 - FUNÇÃO PARA FATORIAL.
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n, show=False):
    '''
    -> Calcula um fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor de um Fatorial de um número n.
    '''
    multiplo_fatorial = 1
    for contador in range(n, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        multiplo_fatorial *= contador
    return multiplo_fatorial


#PROGRAMA PRINCIPAL
numero = int(input('Digite um número para ser o fatorial: '))
print(fatorial(numero, show=True))
