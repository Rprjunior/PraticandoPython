'''104 - VALIDANDO ENTRADA DE DADOS.
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: numero = leiaInt(‘Digite um numero: ‘)'''

def leiaInt(msg):
    ok = False
    while True:
        numero = input(msg)
        if numero.isnumeric():
            numero = int(numero)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok == True:
            break
    return numero


#PROGRAMA PRINCIPAL
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
