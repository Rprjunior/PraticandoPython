'''056 - ANALISADOR
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa.
Mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somar_idade = 0
media_idade = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulher_menor = 0
for pessoas in range(1, 5):
    print('{:^30}'.format('------- {}° PESSOA -------'.format(pessoas)))
    nome = str(input('Digite o {}° nome: '.format(pessoas)))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M] ou [F]: '))
    somar_idade = somar_idade + idade
    if pessoas == 1 and sexo in 'Mn':
        idade_homem_velho = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 18:
        mulher_menor = mulher_menor + 1
print('-'*30)
media_idade = somar_idade / 4
print('O homem mais velho tem \033[:36:40m{}\033[m anos e se chama \033[:36:40m{}\033[m.'.format(idade_homem_velho, nome_homem_velho))
print('A média de idade desse grupo é de \033[:36:40m{:.2f}\033[m anos.'.format(media_idade))
print('Nesse grupo há \033[:36:40m{}\033[m mulheres menores de idade'.format(mulher_menor))
