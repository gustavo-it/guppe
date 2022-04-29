"""
Reversed

OBS: não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

A sua função é inverter o iterável.
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

print(list(reversed(lista)))

# iterando sobre um reversed
for letra in reversed('Docker Container'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print('')
print(''.join(list(reversed('Docker Container'))))

# Podemos tambem utilizar o reversed() para fazer um 'loop' for reverso
for n in reversed(range(0, 10)):
    print(n)
