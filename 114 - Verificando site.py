'''114 - VERIFICANDO SITE.
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    urllib.request.urlopen('http://www.facebook.com')
except urllib.error.URLError:
    print("O site do FACEBOOK não está acessivel no momento.")
else:
    print("Consegui acessar o site do FACEBOOK com sucesso.")
