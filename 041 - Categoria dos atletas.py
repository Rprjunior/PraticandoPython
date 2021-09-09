'''041 - CATEGORIA DOS ATLETAS.
PROGRAMA QUE PERGUNTE O ANO DE NASCIMENTO E MOSTRE EM QUAL CATEGORIA O ATLETA SE ENCAIXA
1 - MIRIM - ATÉ 09 ANOS.
2 - INFANTIL - DE 10 A 14 ANOS.
3 - JUNIOR - DE 15 A 19.
4 - ADULTO - 20+.'''

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Em que ano você nasceu: '))
idade = ano_atual - nascimento
print('Você nasceu no ano de {}, e tem {} anos.'.format(nascimento, idade))
if idade <=9:
    print('Sua categoria é a \033[30mMIRIM.')
elif idade > 9 and idade <=14:
    print('Sua categoria é a \033[1;34mINFANTIL.')
elif idade > 14 and idade <= 19:
    print('Sua categoria é a \033[1;35mJUNIOR.')
elif idade > 19 and idade <=25:
    print('Sua categoria é a \033[1;37mADULTO.')
elif idade >= 26:
    print('Sua categoria é a \033[1;36mMASTER.')

