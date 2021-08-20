'''005 - DISSECANDO UMA VARIAVÉL.
PROGRAMA QUE LEIA UMA STRING E REPASSE INFORMAÇÕES PEDIDAS.'''

a = (input('Qualquer coisa: '))
print('Qual o type de algo:', type(a))
print("É AlphaNumérico?", a.isalnum())
print('É Alpha:', a.isalpha())
print('É Numérico? ', a.isnumeric())
print('É Maisculo? ', a.isupper())
print('É Minusculo', a.islower())
print('Tem espaço?', a.isspace())
