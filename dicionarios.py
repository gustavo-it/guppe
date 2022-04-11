"""
Dicionários

OBS: Em algumas linguagens de programação os dicionários python são conhecidos como
mapas.

Dicionários são coleções do tipo chave/valor.

Chave/valor ficam explícitos

Dicionários são representados por chaves {}

OBS: Sobre dicionários
    -  Chaves e valor são separados por 2 pontos: chave: valor
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

Caso o get não encontre o objeto com a chave informada, será retornado o valor None e não sera gerado KeyEerror

"""
# Criação de dicionários

# Forma 1 (Mais comum)

#        chave: valor
paises = {'br': 'Brasil', 'pt': 'portugal'}
print(paises)
print(paises['br'])

# Forma 2 (Menos comum)
paises2 = dict(br='Brasil', pt='Portugal', eua='Estados Unidos')

print(paises2)

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print('Acessando via chave:', paises2['eua'])

# Forma 2 - Acessando via get - Recomendada
print('Acessando via get:', paises2.get('br'))
print('Acessando via get:', paises2.get('py'))
# OBS: Caso o método get não encontre a chave, ele retornará um tipo de dado None.

pais = paises.get('br')  # Atribuindo ao pais a chave 'br' de paises.
print(f'Encontrei o país {pais}')

pais2 = paises.get('py', 'Não encontrado')  # Nessa variável país pega o país com chave 'py'. Caso não encontre
# Exiba o valor 'Não encontrado'.
print(pais2)

# Verificando se temos essas chaves no dicionário
print('br' in paises)
print('pt' in paises)

if 'br' in paises:
    brasil = paises['br']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário,
# como chaves de dicionários.

# É interessante colocar tuplas como chave de dicionário, pois as tuplas não se alteram.
localidades = {
    (50.6895, 51.6917): 'Escritória em Tókio',
    (60.6895, 61.6917): 'Escritória em Nova York',
    (70.6895, 71.6917): 'Escritória em São Paulo',
    (80.6895, 81.6917): 'Escritória em Belém',
}

print(localidades)

# Adicionar elementos em um dicionário

receita = {'janeiro': 100, 'fevereiro': 120, 'Março': 300}
print(receita)

# Forma 1 - Mais comum
# Coloco o nome do dicionário, crio o nome da chave e defino o valor
receita['Abril'] = 350
print(receita)

# Forma 2
# Criar um novo elemento, adicionar a chave e seu valor
novo_dado = {'maio': 500}
# Acrescentar no dicionário, com o método update, o novo dado
receita.update(novo_dado)  # Mesmo que >>> receita.update({'maio': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['maio'] = 550
print(receita)

# Forma 2
receita.update({'maio': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionário, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

# Forma 1 - Mais comum
# receita.pop('Março') Removendo dados
ret = receita.pop('Março')  # Criando uma variável que vai exibir o valor de março
print('Valor removido:', ret)
print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fevereiro']
print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adiconamos produtos.
"""
Carrinhho compras:
    produto 1:
        - Nome;
        - Preço;
        - Quantidade;
    
    produto 2:
        - Nome;
        - Preço;
        - Quantidade;

"""

# 1 - Utilizando listas

carrinho = []
produto1 = ['Playstantion 4', 1, 230.00]
produto2 = ['God of war', 1, 50.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto

# 2 - Utilizando uma tupla

produto1 = ('Playstantion 4', 1, 2300.00)
produto2 = ('God of war', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto

# 3 - Utilizando dicionário
carrinho = []
produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'nome': 'God of War IV', 'Quantidade': 1, 'Preço': 300.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# Método de dicionários.
d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionário (zerar dados)

d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 - Deep copy
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(novo)
novo['d'] = 4
print(novo)

# Forma 2 - Shallow Copy (Ambas são alteradas)
novo = d

print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
#                      chaves:                       valor das chaves
usuario = {}.fromkeys(['nomes', 'profile', 'senhas'], 'desconhecido')
print(usuario)
# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')  # Transformando cada letra da string em uma chave.
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')  # Transformando cada valor do range em uma chave.
print(veja)
