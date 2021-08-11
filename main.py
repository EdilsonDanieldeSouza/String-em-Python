#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = ''

#sanitização da url

url=url.strip()

#validação da url
if url == '':
    raise ValueError('A url está vazia')

#separa a base e os parâmetros
indice_interogacao= url.find('?')
url_base = url[:indice_interogacao]
url_parametro = url[indice_interogacao+1:]
print(url_parametro)

#busca o valor de um parâmetro
parametro_busca ='moedaOrigem'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor= indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find('&', indice_valor)
if indice_e_comercial == -1:
    valor= url_parametro[indice_valor:]
else:
    valor=url_parametro[indice_valor:indice_e_comercial]

print(valor)