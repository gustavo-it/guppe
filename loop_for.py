"""
Loop for

Loop -> É uma estrutura de repetição.
For -> É uma dessas estruturas.

Python

for item in <conjunto_de_itens>: # item corresponde a cada elemento presente na variável.
    //execução do loop

exemplo de for:
frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)
# O código anterior diz que quero imprimir cada fruta que está dentro da lista frutas.

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.
Basicamente, um objeto iterável é aquele que tem a capacidade de retornar cada um
de seus elementos de forma individual.

Exemplos de iteráveis:
- Strings
    nome = "docker container"

- Lista
    lista = [1, 3, 5, 7]

- Range
    numeros = range(1, 10)

# Exemplo de for 3 (iterando sobre um range)
range(valor_inicial, valor_final)
    for numero in range(1, 10)
        print(numero)


OBS: O valor final não é inclusive.
O valor exibido do range seria:
1
2
3
4
5
6
7
8
9
10 - Não é exibido

nome = "docker"
sobrenome = " container"

# Concatenando strings
print(nome + sobrenome)

# Concatenando com números
print(nome * 3)


# Colocando emojis
emoji = 'U0001F60D'
for num in range(1, 11):
    print('\U0001F60D' * num)
    # \ é um caractere de escape
"""
nome = 'Docker Container' # Temos que transformar em uma lista
lista = [1, 3, 5, 7, 9]
numero = range(1, 10) # Temos que transformar em uma lista


# Exemplo de for 1 (iterando sobre uma string)
for letra in nome: # Para cada letra dentro desse iterável, imprima essa letra
    print(letra)

# Imprimindo toda a string em apenas uma linha
for letra in nome:
    print(letra, end='')


# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

"""
Range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
"""
# Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)

# Descobrindo indice de uma string

for i, v in enumerate(nome):
    print(nome[i])

qtd = int(input("Quantas vezes esse loop deve rodar ?"))
soma = 0

for n in range(1, qtd + 1):  # Incluindo o final do range com '+1'
    numero = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + numero
print(f"A soma é {soma}")