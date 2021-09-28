'''084 - LISTAS, ANÁLISE DE DADOS.
PROGRAMA QUE LEIA NOME E PESO DE FORMA DETERMINADA PELO USUÁRIO.
NO FIM MOSTRE:
1 - NÚMERO DE PESSOAS CADASTRADAS
2 - LISTA DOS MAIS PESADOS
3 - LISTA DOS MAIS LEVES'''

lista = []
lista_final = []
maior_peso = menor_peso = 0

while True:
    lista.append(str(input('Digite um nome: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(lista_final) == 0:
        maior_peso = menor_peso = lista[1]
    else:
        if lista[1] > maior_peso:
            maior_peso = lista[1]
        if lista[1] < menor_peso:
            menor_peso = lista[1]
    lista_final.append(lista[:])
    lista.clear()
    prossiga_1 = str(input('Quer continuar? [S/N]: '))
    if prossiga_1 in 'Nn':
        break

print(f'{lista_final}')
if len(lista_final) == 1:
    print('Apenas uma pessoa foi cadastrada.')
else:
    print(f'Foram cadastradas {len(lista_final)} pessoas.')
print(f'O maior peso foi {maior_peso}kg, de ', end='')
for pessoa in lista_final:
    if pessoa[1] == maior_peso:
        print(pessoa[0])
print(f'O menor peso foi {menor_peso}kg, de ', end='')
for pessoa in lista_final:
    if pessoa[1] == menor_peso:
        print(pessoa[0])
