"""
Map

Com map, fazemos mapeamento de valores para função.
Map recebe dois parãmetros, o primeiro a função, o segundo um iterável.
"""

import math


def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))  # Calculando a área de todos os raios em área.

print(areas)

# Forma 2 --- Map
# Primeiro estou declarando a função area, em segundo pegando a lista de áreas.
# Pega cada valor de raios e passa para função area e colocando os resultados num objeto do tipo map.
areas = map(area, raios)  # Estou calculando os valores de raios.
print(type(areas))
print(list(areas))  # Transformando num lista os valores que obtive calculando os raios.

# Refatorando com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: após utilizar a função map() depois da primeira utilização do resultado, ele zera.
# Só posso utilizar uma vez.

# Para fixar - map

# Temos dados iteráveis:
# dados: a1, a2, ........, an
# Temos uma função:
# Função: f(x)
# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.
# O Map Object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo

# Listas com tuplas
cidades = [
    ('Berlim', 29),
    ('Cairo', 36),
    ('Buenos Aires', 19),
    ('Los Angeles', 26),
    ('Tokio', 27),
    ('Nova York', 27),
    ('Londres', 22)
]

# Transformar em fahrenheit: f = 9/5 * c + 32

# Lambda               retorn da lambda  dado[0] = cidade, dado[1] = temperatura
c_para_f = (lambda dado: (dado[0], (9/5 * dado[1] + 32)))

# map(PASSANDO A FUNÇÃO, ITERÁVEL)
print(list(map(c_para_f, cidades)))

"""
Utilizando uma função

cidades = [
    ('Berlim', 29),
    ('Cairo', 36),
    ('Buenos Aires', 19),
    ('Los Angeles', 26),
    ('Tokio', 27),
    ('Nova York', 27),
    ('Londres', 22)
]

novos_valores = []


def c_para_f():
    for cidade, temperatura in cidades:
        fahrenheit = 9/5 * temperatura + 32
        print(f"{cidade}: {fahrenheit}")
    return ''


print(c_para_f())

# Transformar em fahrenheit: f = 9/5 * c + 32
"""
