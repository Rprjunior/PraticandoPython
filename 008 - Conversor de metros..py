'''008 - CONVERSOR DE METROS
PROGRAMA QUE LEIA UM VALOR E FAÇA SUA CONVERÇÃO ENTRE AS OPÇÕES DE METRAGEM'''

m = float(input('Digite uma valor em metros:'))
km = m / 1000
hm = m / 100
dam = m / 10
mm = m * 1000
cm = m * 100
dm = m * 10
print('Km = {}\nHm ={}\nDm = {}\nMl = {}\nCm = {}\nDe = {} '.format(km, hm, dam, mm, cm, dm))
print('{} Convertido para Km é: {}'.format(m, (m/1000)))
print('{} Convertido para Hm é: {}'.format(m, (m/100)))
print('{} Convertido para Dam é: {}'.format(m, (m/10)))
print('{} Convertido para Mm é: {:.0f}'.format(m, (m*1000)))
print('{} Convertido para Cm é: {:.0f}'.format(m, (m*100)))
print('{} Convertido para Dm é: {:.0f}'.format(m, (m*10)))
