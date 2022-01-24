from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'teste.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do SISTEMA! Até logo.')
        break
    else:
        print('\033[31mERRO! Por favor digite uma opção válida.\033[m')