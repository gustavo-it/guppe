"""
Generators Expression

Ocupam menos espaço na memória.
# Declarando um Generator:
generator = (nome[0] == 'C' for nome in nomes)
"""
# Qual é a utilidade de getsizeof() ? retorna a quantidade de 'bytes' em memória do
# elemento passado como parâmetro.
from sys import getsizeof

nomes = ['Carol', 'Carla', 'Cassandra', 'Cassia']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Mostra quantos 'bytes' a 'string' 'Docker' está ocupando na memória. Quanto maior a 'string'
# Mais espaço ocupa.
print(getsizeof('Docker'))

print(getsizeof('Container'))

print(getsizeof(9))

print(getsizeof(45487812354678786))

print(getsizeof(True))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Iterando sobre o Generator Expression

gen = (x * 10 for x in range(1000))

for numero in gen:
    print(numero)
