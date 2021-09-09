'''039 - ALISTAMENTO MILITAR.
PROGRAMA QUE PERGUNTE UM ANO DE NASCIMENTO E MOSTRE SE A PESSOA TEM IDADE OU NÃO PARA O SERVIÇO MILITAR.'''

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Em que ano você nasceu: '))
idade = ano_atual - nascimento
print('Você nasceu no ano de {} e tem {} anos no ano de {}.'.format(nascimento, idade, ano_atual))
if idade < 18:
    print("Você ainda não tem idade para se alistar AS FORÇAS ARMADAS.")
    alistamento = 18 - idade
    print("Faltará {} ano(s) para seu alistamento".format(alistamento))
    ano_alistamento = alistamento + ano_atual
    print('Você se alistara no ano de {}'.format(ano_alistamento))
elif idade == 18:
    print("Você está na idade certa para se alistar AS FORÇAS ARMADAS.")
else:
    print("Você já ultrassou a idade para alistamento, compareça o quanto antes a uma JUNTA MILITAR")
    alistamento = idade - 18
    print('Você já deveria ter se alistado há {} ano(s)'.format(alistamento))
    ano_alistamento = ano_atual - alistamento
    print('Seu alistamento foi em {}.'.format(ano_alistamento))

