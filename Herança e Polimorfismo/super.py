"""
POO - O método super() 

O método super() se refere a super classe.

"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)  # tenho acesso a qualquer elemento da super classe
        super().faz_som("miau")  # Executando uma função com método super()
        self.__raca = raca

felix = Gato("Felix", "felino", "angorá")
felix.faz_som("miau")
