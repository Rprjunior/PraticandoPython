'''089 - LISTAS, MÉDIA ESCOLAR.
PROGRAMA QUE LEIA POR QUANTAS VEZES QUISER UM NOME E DUAS NOTAS, QUANDO PARA MOSTRE A MÉDIA DE TODOS
NO FIM PERGUNTE SE O USUÁRIO IRÁ QUERER OLHAR AS NOTAS INDIVIDUAIS DE CADA POR NÚMERO CADASTRADO.'''

boletim = list()
print('-'*30)
print(f'{"Escola Cabeça de Porco":^30}')
print('-'*30)
while True:
    nome = str(input('Digite um nome: '))
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    print('-'*30)
    prosseguir_1 = str(input('Quer continuar? [S/N]: '))
    print('-'*30)
    if prosseguir_1 in 'Nn':
        break

print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-'*60)

while True:
    mostrar_nota = int(input('Mostrar notas de qual aluno? (999 Finaliza o programa): '))
    print('-'*60)
    if mostrar_nota == 999:
       print('\033[31mFIM DO PROGRAMA!')
       break
    if mostrar_nota <= len(boletim) - 1:
        print(f'\033[1;33mAs notas de {boletim[mostrar_nota][0]} foram {boletim[mostrar_nota][1]}\033[m.')
        print('-'*60)