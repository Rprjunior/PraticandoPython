'''032 - ANO BISSEXTO.
PROGRAMA QUE LEIA UM ANO QUALQUER E DIGA SE ELE É OU FOI BISSEXTO.'''

from datetime import date
ano = int(input('Digite um ano de sua preferência ou Digite [0] para saber sobre o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('0 ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))

