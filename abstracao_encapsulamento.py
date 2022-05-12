"""
POO — Abstração e Encapsulamento

O grande objetivo da POO é encapsular o nosso código dentro de um grupo lógico e
hierárquico utilizando classes.

Encapsular -> cápsula


            classe
-----------------------------------
|                                 |
|       atributos e métodos       |
|                                 |
-----------------------------------

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        """
        Com parâmetros públicos, podemos alterar os dados de qualquer instância. O que não é indicado
        """
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return "Valor depositádo"
        else:
            return "O valor não é válido"

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                return "Saque efetuado"
            else:
                return "Saldo insuficiente"
        else:
            return "O valor deve ser positivo"

    def transferir(self, valor, conta_destino):
        # Remover o valor da conta
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência

        # Adicionar o valor na conta de destino
        conta_destino.__saldo += valor
        return "Valor transferido"

# Testando


conta1 = Conta("Maria", 150.00, 1500)
conta2 = Conta("Fernanda", 500, 1500)

"""
print(conta1.extrato())
print(conta1.depositar(150))
print(conta1.sacar(100))
print(conta1.extrato())

"""

print(conta2.transferir(100, conta1))
print(conta1.extrato())
print(conta2.extrato())
