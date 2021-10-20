'''090 - DICIONÁRIO EM PYTHON
PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO E MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >=5 and aluno['media'] <7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'

for keys, values in aluno.items():
    print(f' - {keys} é igual a {values}')
