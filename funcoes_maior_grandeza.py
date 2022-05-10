"""
Funções de Maior Grandeza — Higher Order Functions — HOF

O que isso significa?

— Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras
funções, e até mesmo criar variáveis do tipo funções nos nossos programas.

OBS: na se seção de funções, nós utilizamos isso.

Em Python, as funções são cidadões de primeira classe, first class citizen
"""

# Exemplo — Definindo as funções
from random import choice


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas

"""
Em Python também podemos ter funções dentro de funções, que são conhecidas por Nested Functions ou 
também Inner Functions (Funções Internas).
"""

# Exemplo
# importar o random


def cumprimento(pessooa):
    """
    O choice() aleatoriamente irá selecionar uma opção para nós
    Quando a função cumprimento for executada, ela recebe como parâmetro um nome. Em seguida
    a FUNÇÃO INTERNA humor() é executada e vai retornar um dos 3 valores dentro dela.
    Como return final, terei a função humor() + o nome da pessoa.
    """
    def humor():
        return choice(('E ai, ', 'Suma daqui, ', 'Gosto muito de você, '))
    return humor() + pessooa


# Testando função cumprimento

print(cumprimento("Ana Maria"))
print(cumprimento("Angélica"))

# Retornando funções de outras funções
# import random


def faz_me_rir():
    """
    Retornando a função interna rir()
    """
    def rir():
        return choice(("HAHAHAHAHAHHA", "AKKAKAKAKAKA"))
    return rir  # NÃO ESTOU EXECUTANDO A FUNÇÃO


rindo = faz_me_rir()
print(rindo())

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.
# A função humor() pode acessar o escopo da função cumprimento. Ou seja, pode acessar a variável pessoa.


def faz_me_rir_novamente(pessoa):
    """
    Função interna dando_risada(): tenho a variável risada que recebe choice com 3 valores.
    Que retorna a variável risada + pessoa que é um parâmetro da função faz_me_rir_novamente()
    O retorno da função faz_me_rir_novamente() é a função dando risada (QUE NÃO ESTÁ SENDO EXECUTADA)
    """
    def dando_risada():
        risada = choice(("HAHAHAHAHA", "KAKAKAKAKAK", "KKKKKKKKK"))
        return f"{risada} {pessoa}"
    return dando_risada  # NÃO ESTOU EXECUTANDO A FUNÇÃO


# testando faz_me_rir_novamente()

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())  # Executando a variável rindo que recebe uma função
print(rindo())
print(rindo())


