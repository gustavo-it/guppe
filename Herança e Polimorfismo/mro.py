"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de ordem de métodos), é a ordem de execução dos métodos
(quem será executado primeiro).

Em python, a gente pode conferir a ordem de execução dos métodos de 3 formas:
    - Via Propriedade da class __mro__
    - Via método mro()
    - Via help
"""
from heranca_multipla import Pinguim
print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))