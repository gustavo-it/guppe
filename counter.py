"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes


Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a
quantidade de ocorrências desse elemento.

"""
# Realizando o import
from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 4, 4, 4, 5, 5, 45, 45, 43, 43]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)  # Counter({1: 5, 2: 3, 3: 3, 4: 3, 5: 2, 45: 2, 43: 2})

# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2
print(Counter('Docker Container'))
# Counter({'o': 2, 'e': 2, 'r': 2, 'n': 2, 'D': 1, 'c': 1, 'k': 1, ' ': 1, 'C': 1, 't': 1, 'a': 1, 'i': 1})

# Exemplo 3
texto = """ 
 Python é uma linguagem de programação de alto nível,[6] interpretada de script, imperativa, 
 orientada a objetos, funcional, de tipagem dinâmica e forte.
 Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de desenvolvimento 
 comunitário, aberto e gerenciado ela organização sem fins lucrativos Python Software Foundation.
 Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, 
 como um todo, não é formalmente especificada. O padrão de facto é a implementação CPython.
 """
palavras = texto.split()  # Pegando cada palavra e colocando em uma lista (sem palavras repetidas)

# print(palavras)

res2 = Counter(palavras)  # Calculando a ocorrência dessas palavras
print(res2)

# Saber qual palavra mais se repete nesse texto
print(res2.most_common(5))  # Quero as 5 palavras mais comuns
