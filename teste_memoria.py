"""
Teste de Memória com Generators


# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13... (1 + 1 = 2; 2 + 1 = 3; 3 + 2 = 5; 3 + 5 = 8; 5 + 8 = 13;
"""
# Função usando listas 449 MB(utilizado pela memória)


def fib_lista(max):
    """
    variáveis 'a = 0' e 'b = 1'
    enquanto a quantidade de valores na lista números for menor que o número máximo
    acrescente o número b na lista. A variável 'a' irá receber o valor de 'b'
    e a variável 'b' irá receber o valor de 'a + b'. No fim irei retornar a lista(numeros)
    """
    numeros = []
    a, b = 0, 1
    while len(numeros) < max:
        numeros.append(b)
        a, b = b, a + b
    return numeros


print(fib_lista(7))

# Função usando geradores 3 MB(utilizado pela memória)


def fib_gen(max):
    """
    Variáveis 'a = 0', 'b = 1', 'contador = 0'
    enquanto o contador for menor que o valor máximo, a variável 'a' irá receber a variável 'b'
    e a variável 'b' irá receber 'a + b'
    yield vai retornar a variável a em cada loop e contador irá receber contador(0) + 1
    """
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


gen = fib_gen(5)

for n in fib_gen(10):
    print(n)
