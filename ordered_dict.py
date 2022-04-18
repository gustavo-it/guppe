"""
Módulo Collections: Ordered Dict

OrdereDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.
"""
# Em um dicionário a ordem de inserção dos elementos não é garantida.
# Fazendo import
from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave = {chave}: valor = {valor}')

print('')

# Utilizando OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}: valor = {valor}')

# Entendo a diferença entre Dict e Ordered Dict
# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # (True) A ordem dos elementos não importa para os dicionários.

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # (False) A ordem dos elementos importa para o OrderedDict
