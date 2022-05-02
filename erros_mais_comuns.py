"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

1 - SyntaxError _> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, quando escrever
algo que o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError:
a)
def funcao:
    print('Curso de Python')

b)
None = 1

c)
return

2 - NameError _> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError:
a)
print(docker)

b)
docker()

c)
a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)

3 - TypeError _> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError:

a)
print(len(5))

b)
print('Docker' + [])

4 - IndexError _> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo
de dado indexado utilizando um índice inválido.

Exemplos IndexError:

a)
lista = ['Docker']
print(lista[0][10])

b)
lista = ['docker']
print(lista[2])

c)
tupla = ('Docker',)
print(tupla[5])

5 - ValueError _> Ocorre quando uma função/operação built-in (integrada) recebe um argumento
com tipo correto, mas valor inapropriado.

Exemplos ValueError:

a)
print(int('Docker'))

6 - KeyError _> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError:

a)
dic = {}
print(dic['python'])

7 - AttributeError _> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError:

a)
tupla = (2, 4, 61, 10, 54, 3, 1)
print(tupla.sort())

8 - IndentationError _> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError:

a)
def nova():
print('IndentationError')

b)
for i in range(10):
i + 1

OBS: Exceptions e Erros são sinônimos na programação.

OBS: importante ler e prestar atenção na saída de erro.
"""