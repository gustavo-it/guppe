"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[0])

Named Tuple -> São tuplas, diferenciada, onde, especificamos um nome para a mesma e também
parâmetros.
"""
# Importando
from collections import namedtuple
# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='puddle', nome='ray')
print(ray)

# Acessando os dados
# 1º Forma
print(ray[0])  # Declaro a variável e entre colchetes, passo o indice.
print(ray[1])
print(ray[2])

# 2º Forma
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('puddle'))
print(ray.count('puddle'))
