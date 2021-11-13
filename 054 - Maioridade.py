'''054 - MAIORIDADE
'''

from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for vezes in range(1, 6):
    ano_nasc = int(input('Em que ano {}° pessoa nasceu? '.format(vezes)))
    idade = ano_atual - ano_nasc
    print('A sua idade é {} anos'.format(idade))
    if idade >= 18:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1
print('{} JÁ atingiram a maioridade.'.format(maior_idade))
print('{} NÃO atingiram a maioridade.'.format(menor_idade))
