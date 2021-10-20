'''050 - SOMA DE PARES
PROGRAMA QUE LEIA 5 VALORES E FAÇA A SOMA DOS VALORES PARES'''

soma = 0
valores = 0
for repetidor in range(0, 5):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        soma = soma + numero
        valores = valores + 1
print('A soma entre os {} valores pares é: {}'.format(valores, soma))
