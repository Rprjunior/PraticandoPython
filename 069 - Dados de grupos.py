'''PROGRAMA QUE LEIA IDADE E SEXO E PERGUNTE AO USUÁRIO SE QUER CONTINUAR
MOSTRE QUANTOS HOMENS NO TOTAL, MULHERES COM MENOS DE 20 ANOS E E QUANTAS PESSOAS TEM MAIS DE 18 ANOS'''

total18 = homens = mulher20 = 0
print('-=-'*10)
while True:
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ' '


    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        print('-=-' * 10)
    if resp == 'N':
        break

print(f'Foi cadastrado {total18} pessoas com mais de 18 anos.')
print(f'Foi cadastrado {homens} homens.')
print(f'Foi cadastrado {mulher20} mulher(es) com menos de 20 anos.')
