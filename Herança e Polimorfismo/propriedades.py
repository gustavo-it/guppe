"""
POO - Propriedades - Properties


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = Conta.contador + 1

    def extend(self):
        return f"Saindo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        self.__saldo = self.__saldo - valor

    def transferir(self, valor, destino):
        self.__saldo = self.__saldo - valor
        destino.__saldo + valor
    
    
    #get significa "pegar"
    #Estamos criando esses métodos públicos get_ para pegar os valores dos atributos.

                  Por convenção
    -------------------------------------------
    #get_nome_do_atributo ; set_nome_do_atributo

    #set  irá atribuir um novo valor a propriedade.
    
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

conta1 = Conta("Maria", 2500, 5000)
conta2 = Conta("Fernanda", 3000, 5000)

# Fazendo a soma das contas com o método get que está pegando o saldo da conta
soma = conta1.get_saldo() + conta2.get_saldo()
print(soma)

print(conta1.__dict__)
conta1.set_limite(9999)
print(conta1.__dict__)
"""

# Utilizando property
class Conta:
    
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = Conta.contador + 1
    """
    Graças ao decorator property, conseguimos fazer acesso aos valores. É como se fosse um get.
    Pois property simplesmente pega o valor.
    POR PADRÃO, UMA PROPRIEDADE É UM GETTER -> Pega valor
    """
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    """
    Criando um setter para uma propriedade. Colocamos um decorator com o mesmo nome do atributo/propriedade
    seguido de ".setter"
    """
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    """
    Imagine que queira mostrar o valor total (limite + saldo)
    Para isso criei uma função "valor_total" que irá receber saldo e limite, retornando
    a soma dos dois. Lembrando que não tenho um atributo chamado valor_total.
    """

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    def extend(self):
        return f"Saindo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        self.__saldo = self.__saldo - valor

    def transferir(self, valor, destino):
        self.__saldo = self.__saldo - valor
        destino.__saldo + valor

    

conta1 = Conta("Maria", 2500, 5000)
conta2 = Conta("Fernanda", 3000, 5000)

soma = conta1.saldo + conta2.saldo  # Utilizando o property para somar o saldo de duas contas
print(soma)
print(conta1.__dict__)
conta1.limite = 765432  # A propriedade limite o valor vai funcionar como um setter.
print(conta1.__dict__)
print(conta1.limite)  # imprimindo o limite
print(conta1.valor_total)  # Exibindo o valor total da conta
print(conta2.valor_total)  # Note que é uma propriedade e não uma função