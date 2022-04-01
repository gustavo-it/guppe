"""
Loop for

Loop -> É uma estrutura de repetição.
For -> É uma dessas estruturas.

Python

for item in interavel:
    //execução do loop



Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.
objeto iterável -> Ele é qualquer tipo de coisa que você consegue realizar um laço sobre

Exemplos de iteráveis:
- Strings
    nome = "docker container"

- Lista
    lista = [1, 3, 5, 7]

- Range
    numeros = range(1, 10)
"""
nome = 'Docker Container' # Temos que transformar em uma lista
lista = [1, 3, 5, 7, 9]
numero = range(1, 10) # Temos que transformar em uma lista
# Exemplo de for 1
for letra in nome: # Para cada letra dentro desse iterável, imprima essa letra
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
