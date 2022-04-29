"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iteravel
esta vazio.

"""
# Exemplo all()
# print(all([0, 1, 2, 3, 4]))  # False
print(all([1, 2, 3, 4]))  # True

print(all('Docker'))

nomes = ['Cassia', 'Camilla', 'Carla', 'Cristina']

# Verificando se todos os nomes iniciam com a letra 'C' maiúscula.
print(all(nome[0] == 'C' for nome in nomes))

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all(numero for numero in [4, 2, 10, 6, 8] if numero % 2 == 0))

"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro.
Se o iterável estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4, 5]))  # True

print(any([0, False, {}, {}, [], []]))  # False

nomes2 = ['Cassia', 'Camilla', 'Carla', 'Cristina', 'Vanessa']

print(any(nome[0] == 'V' for nome in nomes2))
