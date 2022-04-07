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

lista1.reverse()  # Com slice print(lista1[::-1])
print(lista1)

#  Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#  Descobrir o tamanho de uma lista
print(len(lista1))

#  Podemos remover facilmente o último elemento de uma lista
#  OBS: O pop não somente remove o último elemento, mas também retorna.
print(lista1)
lista1.pop()
print(lista1)

#  Podemos remover um elemento pelo índice.
#  OBS: Os elementos à direita desde índice serão deslocados para a esquerda.
#  OBS: Se não houver elemento no índice informado, teremos o erro indexError.

lista5.pop(2)  # Especificar o índice entre os parênteses.

#  Podemos remover todos os elementos (zerar a lista)
lista5.clear()

#  Posso repetir os elementos em uma lista.
nova = [1, 2, 3]
nova = nova * 3

#  Podemos facilmente converter uma string para uma lista
#  Exemplo 1

curso = 'Programação em Python: Essencial'
curso = curso.split()
print(curso)

#  OBS:  Por padrão, o split separa os lementos da lista pelo espaço entre elas.
#  Exemplo 2
curso = 'Programação, em, python, essencial'
print(curso)
curso = curso.split(',')  # Falando para o split que o separador é uma vírgula.

#  Convertendo uma lista em uma string

lista7 = ['php', 'python', 'html']
curso2 = ' '.join(lista7)  # Definindo um espaço entre os elementos

print(curso2)

#  Iterando sobre listas

#  Exemplo 1:

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)  # Sempre colcoar fora do bloco 'for' o valor final que deseja receber.

#  Exemplo 2(Com string):
lista8 = ['G', 'U', 'G', 'A']
soma = ''
for elemento in lista8:
    print(elemento)
    soma = soma + elemento
print(soma)

#  Exemplo 3 - Utilizando while:

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#  Utilizando variáveis em listas

#  Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'azul', 'amarelo']

print(cores[0])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):  # Enquanto índice for menor que quantida de cores.
    print(cores[indice])  # Imprima cores(lista) dentro do índice
    indice = indice + 1  # indice vai receber indice + 1

#  Fazer acesso aos elementos de forma indexada inversa
#  Para entender melhor o índice negativo, pense na lista como um cículo, onde
#  O final de um elemento está ligado ao início da lista.
print(cores[-1])  # Irá gerar a cor amarelo. Primeiro pegando a lista, depois o índice.

#  Gerar índice em um for
for indice, cor in enumerate(cores):  # Enumerate irá gerar chave e colocar no indice, e gerar valor e colocar na cor.
    print(indice, cor)

#  Listas aceitam valores repetidos

#  Econtrar o indice de um elemento na lista

elemento_lista = [4, 85, 10, 55, 100, 109, 2, 4]

#  Em qual indice está o valor 6
print(elemento_lista.index(6))

#  OBS: Caso não tenha este elemento na lista, será apresentado erro.

#  Caso tenha dois ou mais valores iguais em uma lista, ele irá retornar o índice do primeiro.
print(elemento_lista.index(4))  # Irá retornar o índice 0

#  Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(elemento_lista.index(5, 1))  # Quero que seja encontrado o índice do 5 a partir do valor 1.

#  Podemos fazer busca dentro de um range, início/fim
print(elemento_lista.index(100, 3, 6))  # Busque pra mim o valor 100 entre o índice 3 a 6

#  Revisão do slicing
#  Lista[inicio:fim:passo
#  range[inicio:fim:passo

#  Trabalhando com slice de lista com o parâmetro 'inicio'

lista10 = [1, 2, 3, 4]

print(lista10[1:])  # Iniciando no indice 1 e pegando todo o restante de elementos

print(lista10[:2])  # Começa em 0 e vai até índice 2 - 1, ou seja, não pega o número 3.
# OBS: Caso queira pegar todo o valor da lista, basta acrescentar um número a mais ao índice.
# ex.:
print(lista10[:4])  # Assim irá pegar todos os elementos

print(lista10[1:3])  # Pegando do índice 1 até o 3 - 1, ou seja, não pega o número 4.

#  Trabalhando com slice de lista com o parâmetro 'passo'

print(lista10[1::2])  # Começa no indice 1, vai até o final, de 2 em 2.

print(lista10[::2])  # Começa no indice 0, vai até o final, de 2 em 2.

#  Invertendo valores em uma lista

nomes = ['Docker', 'Container']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

#  Faz a mesma coisa que o exemplo acima
nomes.reverse()
print(nomes)

#  Procurar *soma, *valor máximo, *valor mínimo, tamanho

#  * Se os valores forem todos inteiros ou reais.

lista11 = [1, 2, 3, 4, 5, 6]

print(sum(lista11))  # Soma da lista
print(max(lista11))  # Valor máximo da lista
print(min(lista11))  # Valor mínimo da lista
print(len(lista11))  # Tamanho da lista

#  Transformar lista em tupla
tupla = tuple(lista11)

#  Desenpacotamento de lista
lista11 = [1, 2, 3]
num1, num2, num3 = lista11  # Essas variáveis vão receber os valores da lista

print(num1)
print(num2)
print(num3)

#  Copiando uma lista para outra (Shallow Copy e Deep Copy)
#  Forma 1 Deep Copy
lista12 = [1, 2, 3]
lista14 = lista12.copy()
print(lista14)
lista14.append(4)
print(lista14)
#  Veja que ao utilizarmos lista.copy, copiamos os dados da lista para uma nova lista, mas elas ficaram
# totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em python
#  É chamada de deep copy ou cópia profunda.

#  Forma 2 - Shallow Copy
lista12 = [1, 2, 3]
print(lista12)
lista14 = lista12  # Cópia
lista14.append(4)
print(lista14)
print(lista12)
#  Veja que utilizamos cópia via atribuição e copiamos os dados da lista12 para a lista14, mas após
# após realizer modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em python é chamado de Shallow Copy.
