'''057 - SEXO M OR F
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = input(str('Informe seu sexo: [M/F] - ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = input(str('Dados Inválidos. Por favor, digite seu sexo: [M/F] - ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso.'.format(sexo))
