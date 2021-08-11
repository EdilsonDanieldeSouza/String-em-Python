endereco = 'Rua das Flores 72, Apartamento 1002, Larangeiras, Rio de Janeiro, RJ 23440-120'


import re

padrao =  re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)