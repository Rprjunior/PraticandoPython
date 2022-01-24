'''113 - FUNÇÕES APROFUNDADAS EM PYTHON
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO! Usuário não digitou nenhum valor.\033[m')
            return 0
        else:
            return numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO! Usuário não digitou nenhum valor.\033[m')
            return 0
        else:
            return numero


#PROGRAMA PRINCIPAL
numeroInt = leiaInt('Digite um valor INTEIRO: ')
numeroFloat = leiaFloat('Digite um valor REAL: ')
print(f'O Valor INTEIRO digitado foi {numeroInt} e o valor REAL {numeroFloat}.')