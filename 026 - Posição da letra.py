'''026 - POSIÇÃO DA LETRA.
PROGRAMA QUE LEIA UMA FRASE E MOSTRE
1 - QUANTAS VEZES APARECE UMA LETRA JÁ DEFINIDA.
2 - EM QUAL POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
3 - EM QUAL POSIÇÃO EA APARECE PPOR ÚLTIMO.'''

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Quantas vezes aparece a letra "A": {frase.count("A")}')
print(f'A letra "A" aparece primeiro na posição: {frase.find("A")+1}')
print(f'A letra "A" aparece por último na posição: {frase.rfind("A")+1}')

