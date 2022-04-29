"""
Min e Max

max() _> Retorna o maior valor num iterável ou, o maior de dois ou mais elementos.

min() _> Retorna o menor valor num iterável ou, o menor de dois ou mais elementos.
"""

# Faça um programa que receba dois valores do user e mostre o maior.
# val1 = int(input('Primeiro valor: '))
# val2 = int(input('Segundo valor:'))

# print(max(val1, val2))

# print(max('a', 'b', 'z'))  # Posso usar com 'strings' também

# print(min(val1, val2))

print(min('d', 'c', 'y'))

# Outros exemplos
nomes = ['Arya', 'Maria', 'Ana', 'Fernanda']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "black", "tocou": 3},
    {"titulo": "welcome to the jungle", "tocou": 100},
    {"titulo": "even flow", "tocou": 15},
    {"titulo": "paint black", "tocou": 30},
]
# Imprimir somente o título da música mais e menos tocada
print(f"A música que mais foi tocada: {max(musicas, key=lambda musica: musica['tocou'])['titulo']}")

print(f"A música que menos foi tocada: {min(musicas, key=lambda musica: musica['tocou'])['titulo']}")

"""
# Sem utilizar max, min ou lambdas
maxx = 0
for musica in musicas:
    if musica['tocou'] > maxx:
        maxx = musica['tocou']

for musica in musicas:
    if musica['tocou'] == maxx:
        print(musica['titulo'])

minn = 9999
for musica in musicas:
    if musica['tocou'] < minn:
        minn = musica['tocou']

for musica in musicas:
    if musica['tocou'] == minn:
        print(musica['titulo'])
"""
