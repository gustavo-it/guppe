""""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zem of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora(): #nome simples = inicial maiúscula
    pass


class CalculadoraCientifica(): #nome composto = inicial maiscúla de cada palavra e nome junto
    pass

[2] - Utilize nomes em minusculo, separados por uniderline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar = 5

[3] - Utilize 4 espaços(Não é indicado usar o tab) para identação!

if "a" in "banana":
    print("Tem")

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] Imports

-Imports devem ser sempre feitos em linhas separadas;

Não há problemas em utilizar:

from tupes import Stringype, Listype

Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType
)

Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções
Não faça
funcao( algo[1], {outro: 2 } )

faça
funcao(algo[1], {outro: 2})

[7] - Termine sempre uma instrução com uma nova linha, ou seja, dar um enter.
"""




