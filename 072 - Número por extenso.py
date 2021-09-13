'''072 - Número por extenso.
PROGRAMA QUE PERGUNTE UM VALOR ENTRE 0 E 20 E MOSTRE O RESULTADO POR EXTENSO.'''

contador = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', ' dezenove', 'vinte')

while True:
    numero = int(input('Digite um valor de 0 a 20: '))
    if numero >= 0 and numero <=20:
        break
    print('Número inválido. Tente novamente.')

print(f'O número \033[31m{numero}\033[m por extenso fica \033[32m{contador[numero]}\033[m')
