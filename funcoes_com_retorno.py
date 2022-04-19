"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print {ret_pr}')

# Exemplo função


def quadrado_de_7():  # Esta função não retorna nada
    print(7 * 7)


quadrado_de_7()

OBS: Em Python, quando uma função não reotrna nenhum valor, o retorno é None.

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra
reservada "return".

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos
passar a execução da função para outras funções.

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
"""
# Refatorando(modificar) a função para ela retornar um valor
from random import random


def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função


ret = quadrado_de_7()
print(ret)
print(f'Retorno {quadrado_de_7()}')


# Refatorando a primeira função

def diz_oi():
    return 'oi '


alguem = 'Teste'

print(diz_oi() + alguem)

# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'oi'
  # print('Estou sendo executado depois do retorno')  Nunca será executada


print(diz_oi())


# Exemplo 2

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()  Desempacotando

# print(num1, num2, num3, num4)

print(outra_funcao())  # Irá gerar uma tupla

# Vamos criar uma função para jogar a moeda


def joga_moeda():
    # Gera um número pseudo-rãndomico entre 0 e 1
   # valor = random()
    if random() > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro. mas sim
# codificação desnecessária.


def eh_impar():
    numero = 11
    if numero % 2 != 0:
        return True
    return False  # Não preciso utilizar o else


print(eh_impar())
