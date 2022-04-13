"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos nos referindo a teoria dos conjuntos
da matemática.

- Aqui no python, os conjuntos são denominados como Sets.

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas
não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens
duplicados.

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre Conjuntos (sets) e Mapas (dicionários) em python:
 - Um dicionário tem chave/valor;
 - Um conjunto tem apenas valor;
"""
# Definindo um conjunto:

numeros = [9, 8, 7, 4, 4, 3, 2, 0, 1]  # Os números repetidos serão ignorados e os números serão colocados em ordem
numeros_distintos = set(numeros)

print(type(numeros_distintos))

# OBS: ao criar um conjunto, caso seja lado um valor já existente, o mesmo será ignorado
# sem gerar error e não fará parte do conjunto.
print(numeros_distintos)

if 9 in numeros_distintos:
    print('Econtrei')
else:
    print('Não encontrado')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

lista_numeros = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(lista_numeros)
print(type(lista_numeros))

# Listas aceitam valores duplicados, 'sets' não aceitam

# Assim como todo outro conjunto python podemos colocar todos os tipos de dados misturados em 'Sets'
s = {1, 'python', True, 22, 36}
print(s)
print(type(s))

# Podemos iterar sobre um 'set' normalmente
for valor in s:
    print(f'Valor: {valor}')

# Usos interessantes com 'sets'.

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e então os visitantes
# Infomam manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python. Já que em uma lista podemos adicionar novos elementos
# E ter repetição.

cidades = ['Belo horizonte', 'São Paulo', 'Cuibá', 'Campo grande', 'Cuibá']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas. temos.
print(len(set(cidades)))
print(set(cidades))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorada e não é adicionado.
print(s)

# Remover elementos em um conjunto
# Forma 1
s.remove(3)  # Não é índice! Informamos o valor a ser removido.
print(s)

# OBS: caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2
s.discard(2)
print(s)

# OBS: se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy (Criamos dois elementos independentes com essa técnica)

novo = s.copy()
print(novo)

novo.add(3)
print(novo)

# Forma 2 - Shallow copy
numeros2 = {1, 2, 3, 4}
novo2 = numeros2  # Quero dizer que essas duas variáveis tenham o mesmo valor.
novo2.add(5)
print(novo2)
print(numeros2)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Maria', 'Patricia', 'Sofia', 'João', 'Ryu'}
estudantes_java = {'Fernando', 'Ken', 'Julia', 'Maria', 'Patricia'}

# Veja que alguns alunos que estudam 'Python' também estudam 'Java'

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union (união entre dois conjuntos)
# unicos1 = estudantes_python.union(estudantes_java)
# {'Ken', 'Fernando', 'Maria', 'João', 'Ryu', 'Patricia', 'Sofia', 'Julia'}
# print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)  # Pegamos quem está no curso python e tiramos quem está no jv
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, valor máximo*, valor mínimo*, tamanho
s = {1, 2, 3, 4, 5, 6, 7}
print(sum(s))
print(min(s))
print(max(s))
print(len(s))
