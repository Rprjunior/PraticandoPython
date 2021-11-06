'''062 - P.A. 3.0
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

termo = int(input('Digite o primeiro termo da Progressão: '))
salto = int(input('Digite o valor de salto: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} > '.format(termo), end=' ')
        termo = termo + salto
        contador = contador + 1
    print('LOADING...')
    mais = int(input('Quer mostrar mais termos, quantos?  '))
print('Total de termos mostrados = {}.'.format(total))
print('FIM')
