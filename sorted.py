"""
Sorted

OBS: não confunda, apesar do nome, com a função sort() que ordena os elementos numa lista.
sort() só funciona em listas. Modifica a lista principal.

Podemos utilizar o sorted() com qualquer iterável.
sorted() Não modifica a lista principal
Como o próprio nome diz, sorted() serve para ordernar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenado, porém podemos converter
o resultado para qualquer outra coleção.
"""

numeros = [6, 1, 8, 2]

print(sorted(numeros))  # Ordena do menor para o maior

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para menor

usuarios = [
    {"username": 'Teste', "tweets": ['Vários', 'Testes', 'de', 'tweets']},
    {"username": 'zeni', "tweets": ['Vários', 'de', 'tweets']},
    {"username": 'zeri', "tweets": []},
    {"username": 'sion', "tweets": []},
    {"username": 'garen', "tweets": ['Vários', 'tweets']},
    {"username": 'samira', "tweets": ['de', 'tweets']}
]

print(usuarios)

# Irá ordenar pela quantidade de chaves
print(sorted(usuarios, key=len))

# Ordenando por ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))  # Para inverter basta adicionar 'reverse=True'.

# Ultimo exemplo
musicas = [
    {"titulo": "black", "tocou": 3},
    {"titulo": "welcome to the jungle", "tocou": 100},
    {"titulo": "even flow", "tocou": 15},
    {"titulo": "paint black", "tocou": 30},
]

# Ordenar da música que mais foi tocada para a que menos foi tocada
print(sorted(musicas, key=(lambda musica: musica["tocou"]), reverse=True))

# Ordenar da música que menos foi tocada para a que mais foi tocada
print(sorted(musicas, key=(lambda musica: musica["tocou"])))
