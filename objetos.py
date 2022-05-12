"""
POO — Objetos

Objetos -> São instâncias da classe, ou seja, após o mapeamento do objeto real
para a sua representação computacional, devemos poder criar quantos objetos forem necessários.
Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo definido em classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):  # passando class(cliente) como parâmetro
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        return f"O cliente é {self.__cliente._Cliente__nome}"


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        return f"O cliente {self.__nome} diz oi"


lamp1 = Lampada("branca", 110, 60)
lamp1.ligar_desligar()
print(f"A lâmpada está ligada? {lamp1.checa_lampada()}")
lamp1.ligar_desligar()
print(f"A lâmpada está ligada? {lamp1.checa_lampada()}")

cliente1 = Cliente("Maria Fernanda", "123.545.789-99")
cc = ContaCorrente(5000, 10000, cliente1)  # Passando o limite, saldo e chamando o cliente

print(cc.mostra_cliente())
print(cc._ContaCorrente__cliente.diz())
