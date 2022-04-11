"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

"""

# CUIDADO 1: As tuplas são repersentadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4, )  # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela virgula e não pelo
# uso do parênteses.

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# Gerando tupla com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla6 = ('Docker Container', 'programação em python')  # Definindo valores da tupla

escola, curso = tupla6  # Pegando os valores e colocando nas variáveis em ordem

print(escola)  # Imprimindo valores
print(curso)  # Imprimindo valores

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, valor máximo, valor mínimo* e tamanho (Pode ser calculado mesmo com números e string)

# * Se os valores forem todos inteiros e reais

tupla8 = (1, 2, 3, 4, 5, 6)
print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

# Concatenação de tuplas
tupla9 = 1, 2, 3
print(tupla9)

tupla10 = (4, 5, 6)
print(tupla10)

print(tupla9 + tupla10)  # Tuplas são imutáveis

print(tupla9)
print(tupla10)

# Se quisermos mudar a tupla, temos que fazer do seguinte modo:
tupla11 = tupla9 + tupla10
print(tupla11)

# Tuplas são imutáveis, mas podemos sobrescrever seus valores
tupla9 = tupla9 + tupla10
print(tupla9)

# Verificar se determinado elemento está contido na tupla

print(4 in tupla10)

# Iterando sobre uma tupla
soma = 0
for n in tupla10:
    print(n)
    soma = soma + n
print('A soma é', soma)  # Soma dos valores

# Pegando o indice e o valor da tupla com enumerate
for indice, valor in enumerate(tupla10):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla_string = ('a', 'b', 'c', 'a', 'b', 'b')

print('A quantidade é:', tupla_string.count('b'))

# Convertendo string para tupla
curso = 'Python'
print(curso)
curso2 = tuple(curso)
print(curso2)

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos
# em uma coleção.

# Exemplo 1
meses = 'janeiro', 'fevereiro', 'março', 'abril'

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[1:4])

# Iterar com while (imprimindo todos os meses)
i = 0

while i < len(meses):  # Enquanto i for menor que a quantidade de meses
    print(meses[i])  # imprima meses na posição i
    i = i + 1  # incrementando o i + 1

# Verificamos em qual indice um elemento está na tupla
print('está na posição:', meses.index('março'))

# OBS: Caso o elemento não exista, será gerado erro.

# Slicing

# tupla[inicio:fim:passo]
print(meses[0:4:3])

# Por que utilizar tuplas ?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*. Isso porque trabalhar com elementos imutáveis traz segurança
# para o código.

# Copiando uma tupla para outra

print(tupla9)

nova = tupla9
print(nova)

outra = 13, 12, 11
nova = nova + outra  # Na tupla não temos o problema de Shallow Copy
print(nova)
