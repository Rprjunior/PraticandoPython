'''047 CONTANDO ATÉ 50- '''

print('{:=^30}'.format('\033[035mEscolha uma das opções\033[m'))
print('''[1] Números Ímpares
[2] Números Pares''')
print('='*30)
opcao = int(input('Qual opção você escolhe: '))
if opcao == 1:
    for impar in range(1, 50, +2):
        print(impar, end='  ')
elif opcao == 2:
    for par in range(0, 51, +2):
        print(par, end='  ')
print('Contagem concluída!')
