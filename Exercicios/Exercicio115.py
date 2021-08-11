# Crie um código em Python que teste se o site Pudim
# está acessível pelo computador usado.
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'\033[0;31mErro! Não é possível acessar o site no momento.\033[m')
else:
    print(f'\033[0;34mConsegui! O site do pudim foi acessado com sucesso!.\033[m')
