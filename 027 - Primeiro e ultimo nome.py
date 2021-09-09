'''027 - PRIMEIRO E ULTIMO NOME.
PROGRAMA QUE LEIA UM NOME COMPLETO E MOSTRE APENAS O PRIMEIRO E ÚLTIMO NOME.'''

nome = str(input('Digite seu nome completo: ')).strip()
nome_final = nome.split()
print('Prazer em te conhecer.')
print(f'Seu primeiro nome é: {nome_final[0]}')
print(f'Seu ultimo nome é: {nome_final[len(nome_final)-1]}')

