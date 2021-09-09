'''022 - ANALISADOR DE NOMES.
PROGRAMA QUE LEIA UM NOME E DISTRICHE E MOSTRE ALGUMAS POSSIBILIDADES DO QUE PODE SER FEITO COM STRINGS'''

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome com letras maíusculas fica {nome.upper()}')
print(f'Seu nome em minusculas fica {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)} letras') #Mostra apenas o número de letras no total
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras') #-variavel.count(''). É usado para definir algum caractere que será retirado
separa = nome.split() #Para usar a forma dividida de uma variavel
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
print(f'Seu último nome é {separa[-1]} e tem {len(separa[-1])} letras')
