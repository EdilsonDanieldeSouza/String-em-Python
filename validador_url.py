import re

# https://www.bytebank.com.br/cambio

url = 'www.bytebank.com.br/cambio'
padrão_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrão_url.match(url)

if not match:
    raise ValueError('A URL não é valida')

print('A URL é valida')