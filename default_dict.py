"""
Módulo Collections - Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que podem ou não, receber parâmetros de entrada
e retornar valores.
"""

dicionario = {'curso': 'Python'}
print(dicionario)
print(dicionario['curso'])

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

# print(dicionario)

dicionario['curso'] = 'Python'

print(dicionario)
print(f'Resultado:', dicionario['outro'])  # KeyError no dicionário comum, mas aqui não. O valor é o '0' da função lambda

