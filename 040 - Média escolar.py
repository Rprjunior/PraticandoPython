'''040 - MÉDIA ESCOLAR
PROGRAMA QUE PERGUNTE DUAS NOTAS E MOSTRE A MÉDIA ENTRE ELAS.'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Média = {}\nAluno \033[4;32mAPROVADO'.format(media))
elif media >= 5 and media < 7:
    print('Média = {}\nAluno em \033[4;33mRECUPERAÇÃO'.format(media))
elif media < 5:
    print('Média = {}\nAluno \033[4;31mREPROVADO'.format(media))
