'''036 - APROVANDO EMPRÉSTIMO.
PROGRAMA QUE PERGUNTE O VALOR DO IMOVÉL, O SALÁRIO DO REQUERENTE E EM QUANTO TEMPO PRETENDE PAGAR.
CASO A PARCELA EXCEDA 30% DO VALOR DO SALÁRIO O EMPRÉSTIMO SERÁ NEGADO.'''

valor_da_casa = float(input("Qual o valor da casa desejada: "))
salario = float(input("Qual seu salário: "))
tempo = float(input("Em quantos anos pretende pagar: "))
parcela = valor_da_casa / (tempo * 12)
teto_porcentagem = (salario / 100) * 30
if parcela > teto_porcentagem:
    print("EMPRÉSTIMO NEGADO!\nO valor da parcela ultrapassou o teto de porcentagem para seu salário.")
else:
    print('EMPRÉSTIMO CONCEDIDO!\nSerão {} parcelas de: R${:.2f}'.format(tempo * 12, parcela))

