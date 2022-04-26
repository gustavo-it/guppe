"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas. São funções sem nome, ou seja,
funções anônimas.

"""


# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda

# Recebe um parâmetro(o 'x') e retorna 3 * x + 1
# lambda x: 3 * x + 1

# E como utilizar a expressão Lambda?

calc = (lambda x: 3 * x + 1)

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas

# Possui duas entradas (nome e sobrenome), ela retorna o nome + espaço + sobrenome
#  .Strip() remove os espaços que podem ocorrer no início e fim da variável.
nome_completo = (lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title())

print(nome_completo(' gustavo', ' CASTRO'))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

docker = (lambda: 'Como não gostar de docker ?')

uma = (lambda x: 3 * x + 1)

duas = (lambda x, y: (x * y) ** 0.5)

tres = (lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z))

# n = (lambda x1, x2, ....., xn: <expressão>)

print(docker())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo

autores = [
    'Isaac Asimov',
    'Ray Bradbury',
    'Robert Heinlein',
    'Arthur C. Clarke',
    'Frank Hebert',
    'Orson Scott Card',
    'Douglas Adams',
    'H.G Wells',
    'Leigh Brackett'
]

print(autores)

# Ordernar(autores) pelo sobrenome
# lambda irá receber o sobrenome, vamos pegar o sobrenome e usar o split para separar o espaço e com -1
# pegamos o último elemento. Lower() deixa tudo em minúsculo.
# Key determinado uma função que vai ser usada em cada elemento da lista
autores.sort(key=(lambda sobrenome: sobrenome.split(' ')[-1].lower()))

print(autores)


def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

# Passando o valor de x
print(teste(0))
print(teste(1))
print(teste(2))

# Acrescentando o x no final
print(geradora_funcao_quadratica(3, 0, 1)(2))

# Aplicamos lambdas para fazer filtragem e ordenação de dados
