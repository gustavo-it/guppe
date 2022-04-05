"""
Listas python

Listas em python funcionam como vetores/matrizes (arrays) em outras línguas.
Com a diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado

- Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente
ir adicionando elementos.
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer
tipo de dado.

As listas em python são representadas por colchetes: []

"""
lista1 = [10, 25, 34, 22, 55, 6, 79]

lista2 = ['A', 'D', 'C', 'F', 'K', 'Z', 'A']

lista3 = []

lista4 = list(range(11))

lista5 = list('Docker Container')

#  Podemos facilmente juntar 2 listas

lista6 = lista1 + lista2  # Faz a mesma coisa que extend

# Podemos facilmente checar se determinado valor está contido na lista
numero = int(input('Digite o número que deseja encontrar: '))
if numero in lista1:
    print(f'Encontrei o número {numero}')
else:
    print(f'Não encontrei o número {numero}')


# Podemos checar em string também
letra = input('Digite a letra que deseja checar: ')
if letra in lista5:
    print(f'Econtrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')


#  Podemos facilmente ordernar uma lista
lista1.sort()  # Primeiros devemos ordernar
print(lista1)


#  Ordenando uma lista de string
lista2.sort()
print(lista2)


#  Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))  # Quero contar na lista 1, quantas vezes o número se repete.
print(lista2.count('A'))  # Quero contar na lista 2, quantas vezes a letra 'A' se repete.


#  Adicionar elementos em listas
"""
Para adicionar elementos ou valores em listas, utilizamos a função append()

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez.

"""
print(lista1)
lista1.append(42)
print(lista1)

#  Posso colocar um elemento do tipo lista com append.

lista1.append([8, 3, 1])  # Adicionando uma lista com append. Coloca a lista como elemento único [sublista]
print(lista1)

if [8, 3, 1] in lista1:  # Verificando se existe o conjunto na lista.
    print('Encontrei os números.')
else:
    print('Não encontrei os números.')

lista1.extend([123, 44, 67])  # Faz a mesma coisa que o append. Coloca cada elemento da lista como valor adicional
print(lista1)  # extend não aceita valor único

#  Podemos inserir um novo elemento na lista informando a posição do índice
inserir_na_lista = input('Digite aqui o valor que você deseja colocar na lista: ')
lista1.insert(0, inserir_na_lista)  # insert(definindo_a_posição, dados)
print(lista1)

#  Podemos facilmente inverter uma lista

lista1.reverse()
print(lista1)  # Com slice print(lista1[::-1])
