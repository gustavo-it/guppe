"""
Preservando metadatas com wraps

Metadados(metadata) -> São dados intrisecos(dados internos) em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.


"""
from functools import wraps
# Problema Enviando o nome da função/documentação da função principal, quando, na verdade, quero da funçaõ interna

"""
def ver_log(funcao):
    def logar(*args, **kwargs):
        ""Eu sou uma função(logar) dentro de outra""
        print(f'Você está chamando: {funcao.__name__}')  # retorna o nome da função vindo como parâmetro
        print(f"Aqui a documentação: {funcao.__doc__}")  # Retorna a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    ""Soma dois números.""
    return a + b


print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)
"""

# Resolução do problema
# from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # Basta adicionar esse decorator a função
    def logar(*args, **kwargs):
        """Eu sou uma função(logar) dentro de outra"""
        print(f'Você está chamando: {funcao.__name__}')  # retorna o nome da função vindo como parâmetro
        print(f"Aqui a documentação: {funcao.__doc__}")  # Retorna a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)
