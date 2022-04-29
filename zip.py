"""
Zip

zip() _> Cria um iterável (zip object) que agrega elemento de cada um dos iteráveis
passados como entrada em pares.
"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionario

print(list(zip1))

zip1 = zip(lista1, lista2)

print(dict(zip1))

# OBS: O zil() utiliza como parãmetro o menor tamanho em iterável. Isso significa que
# se for trabalhar com iteráveis  de tamanhos diferentes. Irá parar quando os elementos
# do menor iterável acabar.
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))  # É eliminado os valores que esta sobrando

# Podemos utilizar diferentes iteráveis com zip()

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (2, 3), (4, 5)]
print(list(zip(*dados)))

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Fernanda', 'jaque']
# Chave: alunos[0]: prova 1,   prova2  para dado in zio(alunos, prova1, prova2)
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Para entender melhor o exemplo anterior. Estou pegando alunos na posição 0
# Verificando entre prova1 e prova2 qual nota é maior
# pegando cada linha que esta dentro de zip()
zt2 = list(zip(alunos, prova1, prova2))
print(zt2)

# Utilizando map
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final2))
