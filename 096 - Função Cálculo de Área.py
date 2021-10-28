'''096 - FUNÇÃO CÁLCULO D ÁREA
PROGRAMA QUE TENHA UMA FUNÇÃO DE NOME ÁREA, QUE RECEBA LARGURA E COMRPIMENTO E MOSTRE ÁREA DO TERRENO.'''

def area(largura, comprimento):
    metragem = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {metragem} m².')


#PROGRAMA PRINCIPAL
print('-'*30)
print(f'{"CONTROLE DE TERRENOS" :^30}')
print('-'*30)
larg = float(input('Largura em metros: '))
comp = float(input('Comprimento em metros: '))
area(larg, comp)
