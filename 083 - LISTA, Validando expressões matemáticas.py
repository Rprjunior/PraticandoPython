'''083 - LISTA, VALIDANDO EXPRESSÕES MATEMÁTICAS.
PROGRAMA QUE LEIA UMA EXPRESSÃO QUE USE PARENTESES E INFORME SE
A EXPRESSÃO TEM A MESMA QUANTIDADE DE PARENTESES ABERTOS E FECHADOS.'''

expressao = str(input('Digite uma expressão: '))
lista_caractere = []

for caractere in expressao:
    if caractere == '(':
        lista_caractere.append('(')
    elif caractere == ')':
        if len(lista_caractere) > 0:
            lista_caractere.pop()
        else:
            lista_caractere.append(')')
            break

if len(lista_caractere) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida, PARENTESES desiguais.')