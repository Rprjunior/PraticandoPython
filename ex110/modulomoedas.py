'''Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

def aumentar(preco = 0, taxa = 0, formato = False):
    resultado = preco + (preco * taxa/100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preco = 0, taxa = 0, formato = False):
    resultado = preco - (preco * taxa/100)
    return resultado if formato is False else moeda(resultado)


def dobro(preco = 0, formato = False):
    resultado = preco * 2
    return resultado if formato is False else moeda(resultado)


def metade(preco = 0, formato = False):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco = 0, taxaAumento = 10, taxaReducao = 5):
    print('-'*35)
    print('{:^30}'.format('RESUMO DE VALORES'))
    print('-'*35)
    print(f'O preço analisado: \t\t{moeda(preco)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
    print(f'Com {taxaAumento}% de aumento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'Com {taxaReducao}% de desconto: \t{diminuir(preco, taxaReducao, True)}')
    print('-'*35)
