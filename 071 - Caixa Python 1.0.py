print('='*30)
print('{:^30}'.format('BANCO DIGITAL'))
print('='*30)

saque = int(input('Qual o valor do saque. R$ '))
cedula = 100
total_cedulas = 0

while True:
    if saque >= cedula:
        saque = saque - cedula
        total_cedulas = total_cedulas + 1
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} cédula(s) de R$ {cedula}.')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        total_cedulas = 0
        if saque == 0 or saque == 1:
            break
print('='*30)
print('{:^30}'.format('OPERAÇÃO FINALIZADA'))
print('{:^30}'.format('VOLTE SEMPRE'))