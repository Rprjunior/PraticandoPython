''' 025 - DESCOBRINDO SOBRENOME.
PROGRAMA QUE LEIA UM NOME E DESCUBRA SE HÁ UM SOBRENOME OU UMA LETRA DEFINIDOS.'''

sobrenome = str(input('Digite seu nome completo: ')).strip()
print(f'No seu nome há o sobrenome "PEREIRA": {"pereira" in sobrenome.lower()}')

palavra = str(input('Digite um palavra qualquer: ')).strip()
print(f'Nesse nome há a letra "A": {"A" in palavra.upper()}')
