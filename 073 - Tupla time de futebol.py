'''073 - TUPLA TIME DE FUTEBOL
CRIE UMA TUPLA COM A CLASSIFICAÇÃO DO CAMPEONATO BRASILEIRO 2021.
MOSTRE:
1 - OS 5 PRIMEIROS
2 - OS 4 ÚLTIMOS
3 - TODOS OS CLUBES EM ORDEM ALFABÉTCA
4 - QUAL A POSIÇÃO DO MENGÃO'''

times = ('FLAMENGO', 'ATLÉTICO - MG', 'PALMEIRAS', 'FORTALEZA', 'BRAGANTINO',
         'CORITNHIANS', 'FLUMINENSE', 'CUIABÁ', 'ATLÉTICO - GO', 'ATLÉTICO - PR',
         'CEARÁ', 'INTERNACIONAL', 'SANTOS', 'JUVENTUDE', 'BAHIA',
         'SÃO PAULO', 'AMÉRICA - MG', 'GRÊMIO', 'SPORT', 'CHAPECOENSE')

print(f'Os 05 primeiro colocados são? \n{times [0:5]}')
print(f'Os 04 últimos colocados são? \n{times [-4:]}')
print(f'Clubes em ordem alfabética: {sorted(times)}')
print(f'A posição do MENGÃO é a {times.index("FLAMENGO")+1}°')
