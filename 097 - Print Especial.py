'''097 - PRINT ESPECIAL
PROGRAMA QUE TENHA UMA FUNÇÃO ESCREVA() QUE RECEBA QUALQUER TEXTO E ADAPTE LINHAS DO TAMANHO DO TEXTO.'''

def escreva(msg):
    tam = len(msg) + 10
    print('-'*tam)
    print(f'     {msg}')
    print('-' * tam)


#PROGRAMA PRINCIPAL
escreva('CURSO DE PYTHON')
escreva('INTELIGÊNCIA ARTIFICIAL')
escreva('BANCO DE DADOS MYSQL')
