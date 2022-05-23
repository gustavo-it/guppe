"""
POO - Polimorfismo

Poli -> Muitas
morfis -> Formas

Quando a gente reemplementa um método presente na class pai em classes filhas
estamos realizando uma sobrescrita de método (Overrading).

O overrading é a melhor representação do polimorfismo.
"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    
    def falar(self):
        """
        Implementar este método nas classes filhas
        """
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        """
        Reemplementando o método falar da class Animal
        """
        print("{self._Animal__nome} está falando..")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        """
        Reemplementando o método falar da class Animal
        """
        print(f"{self._Animal__nome} está falando")


class Hamster(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} está falando")


# Testes para

felix = Gato("felix")
felix.comer()
felix.falar()

cachorro = Cachorro("Pluto")
cachorro.comer()
felix.falar()

hamster = Hamster("Gado")
hamster.comer()
hamster.falar()
