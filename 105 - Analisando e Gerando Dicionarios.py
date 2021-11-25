'''105 - ANALISANDO E GERANDO DICIONÁRIOS
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''

def notas(*n, result=False):
    informacoes = dict()
    informacoes['TOTAL'] = len(n)
    informacoes['MAIOR'] = max(n)
    informacoes['MENOR'] = min(n)
    informacoes['MÉDIA'] = sum(n) / len(n)
    if result:
        if informacoes['MÉDIA'] >= 7:
            informacoes['SITUAÇÃO'] = 'BOA.'
        elif informacoes['MÉDIA'] >= 5 and informacoes['MÉDIA'] < 7:
            infomracoes['SITUAÇÃO'] = 'RAZOÁVEL.'
        else:
            informacoes['SITUAÇÃO'] = 'RUIM.'
    return informacoes


#PROGRAMA PRINCIPAL
total = notas(5, 6, 9, 10, result=True)
print(total)
