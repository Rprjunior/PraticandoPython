'''024 - CIDADE 'SANTO'.
PROGRAMA QUE LEIA UM NOME DE UMA CIDADE E MOSTRE SE ELA TEM O NOME SANTO.'''

cidade = str(input('Em qual cidade você nasceu: ')).strip()
print(f'A cidade que você nasceu tem o nome Santo no inicio? {(cidade[:5].lower() == "santo")}')
