"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;
"""

# Exemplo 1 - Multiderivação Direta

from unicodedata import name


class Base1:
    pass

class Base2:
    pass

class Multiderivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

#OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdara
# todos os atributos e métodos das super classe.

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
        return f"Eu sou {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando."

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar!"

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome}"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

    
if __name__ == "__main__":
    baleia = Aquatico("docker")
    print(baleia.nadar())
    print(baleia.cumprimentar())

    tatu = Terrestre("xin")
    print(tatu.andar())
    print(tatu.cumprimentar())

    linux = Pinguim("linux")
    print(linux.andar())
    print(linux.cumprimentar())
    print(linux.nadar())  # Method Resolution Order - MRO Está executando o método da class Terrestre

    # Objeto é uma instância de...
    print(f"linux é instância de pinguim ? {isinstance(linux, Pinguim)}")  # True
    print(f"linux é instância de Aquatico ? {isinstance(linux, Aquatico)}")  # True
    print(f"linux é instância de Terrestre ? {isinstance(linux, Terrestre)}")  # True
    print(f"linux é instância de object ? {isinstance(linux, object)}")  # True
    print(f"linux é instância de Animal ? {isinstance(linux, Animal)}")  # True