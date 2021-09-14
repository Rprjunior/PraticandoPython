'''077 - C0NTANDO VOGAIS EM TUPLAS.
PROGRAMA QUE MOSTRE UMA LISTA EM TUPLA E LOGO MOSTRE APENAS SUA VOGAIS.'''

palavras = ('Carro', 'Moto', 'Caminhão', 'Onibus', 'Carreta',
            'Barco', 'Navio', 'Lancha', 'Jet-Ski', 'Submarino')

for palavra in palavras:
    print(f'\nPara a palavra {palavra.upper()} temos as vogais: ', end='')
    for vogais in palavra:
        if vogais.lower() in 'aeiou':
            print(vogais.lower(), end=' ')
