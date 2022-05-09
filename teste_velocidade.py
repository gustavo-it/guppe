"""
Teste de velocidade com expressões geradoras
"""
import time
# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1, 10))  # printa o número para cada numero in range
print(next(ge2))

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(1000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(1000000)]))
list_tempo = time.time() - list_inicio

print(f"Generator expression levou {gen_tempo}")
print(f"List comprehension levou {list_tempo}")
