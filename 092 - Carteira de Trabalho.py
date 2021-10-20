'''092 - CARTEIRA DE TRABALHO
PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E NÚMERO DA CARTEIRA DE TRABALHO
SE A CTPS FOR DIFERENTE DE ZERO, TAMBÉM LEIA ANO DE CONTRATAÇÃO E O SALÁRIO
CALCULE E MOSTRE ALÉM DA IDADE COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR'''

from datetime import datetime

dados = dict()
dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho / [0] - Não tem: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano do primeiro contrato: '))
    dados['salario'] = float(input('Salário atual: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('-'*30)
print(f'{"RESULTADO":^30}')
print('-'*30)

for keys, values in dados.items():
    print(f' - {keys} tem valor {values}')