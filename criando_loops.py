"""
Criando a sua própria versão de 'loop'
"""


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for("Python do básico ao avançado")
